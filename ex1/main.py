#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard, CreatureArg
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard, SpellArg
from ex1.ArtifactCard import ArtifactCard, ArtifactArg


def main_ex1():
    print("=== DataDeck Deck Builder ===")
    print()
    print("Building deck with different card types...")
    cards = [
        SpellCard(*SpellArg.LIGHTNING.value),
        ArtifactCard(*ArtifactArg.MANA_CRYSTAL.value),
        CreatureCard(*CreatureArg.FIRE_DRAGON.value)
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
