from ex0.Card import Card
import random


class Deck():
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards += [card]

    def remove_card(self, card_name: str) -> bool:
        original_count = len(self.cards)
        self.cards = [card for card in self.cards if card.name != card_name]
        return len(self.cards) < original_count

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("Cannot draw from empty deck")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        count = 0
        total_cost = 0
        creatures = 0
        spells = 0
        artifacts = 0

        for card in self.cards:
            count += 1
            total_cost += card.cost
            if card.CARD_TYPE == "Creature":
                creatures += 1
            elif card.CARD_TYPE == "Spell":
                spells += 1
            elif card.CARD_TYPE == "Artifact":
                artifacts += 1
        avg_cost = round(total_cost/count, 0) if count else 0

        return {
            "total_cards": count,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }
