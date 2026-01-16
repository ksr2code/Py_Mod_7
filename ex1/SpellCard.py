from ex0.Card import Card
from enum import Enum


class SpellArg(Enum):
    FIREBALL = ("Fireball", 4, "Uncommon", "damage")
    LIGHTNING = ("Lightning Bolt", 3, "Common", "damage")


class SpellCard(Card):
    CARD_TYPE = "Spell"

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        match self.effect_type:
            case "damage":
                effect = "Deal 3 damage to target"
            case "heal":
                effect = "Restore 3 health to target"
            case "buff":
                effect = "Buff target"
            case "debuff":
                effect = "Debuff target"
            case _:
                effect = "Undefined"

        if self.is_playable(game_state["mana"]):
            game_state["mana"] -= self.cost
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": effect
            }
        return {'card_played': None, 'error': 'Insufficient mana'}

    def resolve_effect(self, targets: list) -> dict:
        total_damage = 0
        survivors = []
        for target in targets:
            target.health -= 3
            total_damage += 3
            if target.health > 0:
                survivors += [target]
        return {
            "spell": self.name,
            "targets": [target.name for target in targets],
            "damage_dealt": total_damage,
            "combat_resolved": False if survivors else True
        }
