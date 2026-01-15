from abc import ABC, abstractmethod


class Combatable(ABC):
    SIGNATURES = ['attack', 'defend', 'get_combat_stats']

    @abstractmethod
    def attack(self, target) -> dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass
