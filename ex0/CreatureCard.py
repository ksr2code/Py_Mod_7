from ex0 import Card


class CreatureCard(Card):
    CARD_TYPE = "Creature"

    def __init__(
            self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["mana"]):
            game_state["mana"] -= self.cost
            game_state["battlefield"] += [self]
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }
        else:
            return {
                "card_played": None,
                "error": f"Insufficient mana: {self.cost} required"
            }

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": self.attack >= target.health
        }

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info["attack"] = self.attack
        card_info["health"] = self.health
        return card_info
