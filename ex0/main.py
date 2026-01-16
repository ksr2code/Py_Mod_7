#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard, CreatureArg


def main_ex0():
    try:
        print("=== DataDeck Card Foundation ===")
        print()
        print("Testing Abstract Base Class Design:")
        print()
        card_1 = CreatureCard(*CreatureArg.FIRE_DRAGON.value)
        card_2 = CreatureCard(*CreatureArg.GOBLIN.value)
        print("CreatureCard Info:")
        print(f"{card_1.get_card_info()}")
        print("Playing Fire Dragon with 6 mana available:")
        game_state = {"mana": 6, "battlefield": []}
        print(f"Playable: {card_1.is_playable(game_state["mana"])}")
        print(f"Play result: {card_1.play(game_state)}")
        print()
        print("Fire Dragon attacks Goblin Warrior:")
        print(f"Attack result: {card_1.attack_target(card_2)}")
        print()
        print("Testing insufficient mana (3 available):")
        game_state = {"mana": 3, "battlefield": []}
        print(f"Playable: {card_1.is_playable(game_state["mana"])}")
        print()
        print("Abstract pattern successfully demonstrated!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main_ex0()
