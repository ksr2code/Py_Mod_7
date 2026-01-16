from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class FantasyCardFactory(CardFactory):
    _creatures = {
        7: CreatureCard("Fire Dragon", 5, "Legendary", 7, 5),
        2: CreatureCard("Goblin Warrior", 2, "Common", 2, 1),
    }

    _spells = {
        4: SpellCard("Fireball", 4, "Uncommon", "damage"),
        3: SpellCard("Lightning Bolt", 3, "Common", "damage"),
    }

    _artifacts = {
        2: ArtifactCard("Mana Crystal", 2, "Common", 5,
                        "Permanent: +1 mana per turn"),
        4: ArtifactCard("Ring of Wisdom", 4, "Rare", 4,
                        "Permanent: Draw an extra card each turn")
    }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            creature_map = {
                "dragon": self._creatures[7],
                "goblin": self._creatures[2],
            }
            return creature_map.get(name_or_power, self._creatures[7])
        elif isinstance(name_or_power, int):
            return self._creatures.get(name_or_power, self._creatures[7])
        return random.choice(list(self._creatures.values()))

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            spell_map = {
                "fireball": self._spells[4],
                "lightning bolt": self._spells[3],
            }
            return spell_map.get(name_or_power, self._spells[3])
        elif isinstance(name_or_power, int):
            return self._spells.get(name_or_power, self._spells[4])
        return random.choice(list(self._spells.values()))

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            artifact_map = {
                "mana_crystal": self._artifacts[2],
                "wisdom_ring": self._artifacts[4],
            }
            return artifact_map.get(name_or_power, self._artifacts[2])
        elif isinstance(name_or_power, int):
            return self._artifacts.get(name_or_power, self._artifacts[2])
        return random.choice(list(self._artifacts.values()))

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        card_types = ['creature', 'spell', 'artifact']
        for _ in range(size):
            card_type = random.choice(card_types)
            if card_type == 'creature':
                deck.append(self.create_creature())
            elif card_type == 'spell':
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())
        return {
            'factory': 'FantasyCardFactory',
            'deck_size': size,
            'deck': deck
        }

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_crystal']
        }
