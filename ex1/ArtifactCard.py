from ex0.Card import Card


class ArtifactCard(Card):
    CARD_TYPE = "Artifact"

    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["mana"]):
            game_state["mana"] -= self.cost
            if "artifacts" not in game_state:
                game_state["artifacts"] = []
            game_state["artifacts"].append(self)

            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": f"Permanent: {self.effect}"
            }
        else:
            return {
                "card_played": None,
                "error": f"Insufficient mana: {self.cost} required"
            }

    def activate_ability(self) -> dict:
        if self.durability > 0:
            self.durability -= 1
            return {
                "artifact": self.name,
                "effect": self.effect,
                "durability_remaining": self.durability,
                "ability_activated": True
            }
        else:
            return {
                "artifact": self.name,
                "error": "Artifact exhausted (durability: 0)",
                "ability_activated": False
            }
