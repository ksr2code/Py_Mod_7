#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


def main_ex1():
    print("=== DataDeck Deck Builder ===")
    print()
    print("Building deck with different card types...")
    cards = [
        SpellCard("Lightning Bolt", 3, "Common", "damage"),
        ArtifactCard("Mana Crystal", 2, "Common", 5,
                     "Permanent: +1 mana per turn"),
        CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    ]
    deck = Deck()
    for card in cards:
        deck.add_card(card)
    print(f"Deck stats: {deck.get_deck_stats()}")
    print()
    print("Drawing and playing cards:")
    print()
    while deck.cards:
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.CARD_TYPE})")
        print(f"Play result: {card.play({'mana': 10, 'battlefield': []})}")
        print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main_ex1()
