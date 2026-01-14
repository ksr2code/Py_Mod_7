from ex0 import Card


class CreatureCard(Card):
    CARD_TYPE = "Creature"

    def __init__(
            self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        pass

    def attack_target(self, target) -> dict:
        pass

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info["attack"] = self.attack
        card_info["health"] = self.health
        return card_info
