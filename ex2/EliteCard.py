from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from enum import Enum


class EliteArg(Enum):
    ARCANE_WARRIOR = ("Arcane Warrior", 5, "Legendary")
    ENEMY = ("Enemy", 2, "Common", 2, 1)


class EliteCard(Card, Combatable, Magical):
    CARD_TYPE = "Elite"

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state.get("mana", 0)):
            game_state["mana"] -= self.cost
            game_state["battlefield"] += [self]
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Elite card summoned to battlefield'
            }
        return {'card_played': None, 'error': 'Insufficient mana'}

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': 5,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            'defender': self.name,
            'damage_taken': incoming_damage - 3,
            'damage_blocked': 3,
            'still_alive': True
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack_power': 5,
            'defense': 5,
            'health': 10
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': 4
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            'channeled': amount,
            'total_mana': amount + 4
        }

    def get_magic_stats(self) -> dict:
        return {
            'mana_pool': 100,
            'magic_power': 4
        }
