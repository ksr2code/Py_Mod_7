from abc import ABC, abstractmethod


class Magical(ABC):
    SIGNATURES = ['cast_spell', 'channel_mana', 'get_magic_stats']

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        pass
