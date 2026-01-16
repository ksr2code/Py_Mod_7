#!/usr/bin/env python3

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex2.Combatable import Combatable
from ex2.EliteCard import EliteCard, EliteArg
from ex2.Magical import Magical


def main_ex2():
    print("=== DataDeck Ability System ===")
    print()
    print("EliteCard capabilities:")
    print(f"- Card: {Card.SIGNATURES}")
    print(f"- Combatable: {Combatable.SIGNATURES}")
    print(f"- Magical: {Magical.SIGNATURES}")
    print()
    print("Playing Arcane Warrior (Elite Card):")
    elite = EliteCard(*EliteArg.ARCANE_WARRIOR.value)
    enemy = CreatureCard(*EliteArg.ENEMY.value)
    print()
    print("Combat phase:")
    print(f"Attack result: {elite.attack(enemy)}")
    print(f"Defense result: {elite.defend(5)}")
    print()
    print("Magic phase:")
    print(f"Spell cast: {elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {elite.channel_mana(3)}")
    print()
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main_ex2()
