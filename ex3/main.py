#!/usr/bin/env python3

from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine, GameArg


def main_ex3():
    print("=== DataDeck Game Engine ===")
    print()
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game = GameEngine()
    game.configure_engine(factory, strategy)
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Avaliable types: {factory.get_supported_types()}")
    print()
    print("Simulating aggressive turn...")
    print(f"Hand: {GameArg.HAND.value}")
    print()
    print("Turn execution:")
    for k, v in game.simulate_turn().items():
        print(f"{k}: {v}")
    print()
    print("Game Report:")
    print(f"{game.get_engine_status()}")
    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main_ex3()
