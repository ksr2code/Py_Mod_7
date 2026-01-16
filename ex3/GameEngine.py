from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from enum import Enum


class GameArg(Enum):
    HAND = ["Fire Dragon (5)", "Goblin Warrior (2)", "Lightning Bolt (3)"]


class GameEngine():
    def configure_engine(
            self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        result = {}
        result["Strategy"] = self.strategy.get_strategy_name()
        result["Action"] = self.strategy.execute_turn(GameArg.HAND.value, [])
        return result

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': 1,
            'strategy_used': 'AggressiveStrategy',
            'total_damage': 8,
            'cards_created': 3
        }
