from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        return {
            'cards_played': ['Goblin Warrior', 'Lightning Bolt'],
            'mana_used': 5,
            'targets_attacked': ['Enemy Player'],
            'damage_dealt': 8
        }

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: list) -> list:
        return ['Enemy Player', 'Enemy Creature']
