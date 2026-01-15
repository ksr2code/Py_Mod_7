from ex0.Card import Card


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
        else:
            return {
                "card_played": None,
                "error": f"Insufficient mana: {self.cost} required"
            }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "targets": [target.name for target in targets],
            "effect_type": self.effect_type,
        }
