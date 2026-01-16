from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from enum import Enum
import random


class Arg(Enum):
    FIRE_DRAGON = ("Fire Dragon", 5, "Legendary", 7, 5)
    GOBLIN = ("Goblin Warrior", 2, "Common", 2, 1)
    FIREBALL = ("Fireball", 4, "Uncommon", "damage")
    LIGHTNING = ("Lightning Bolt", 3, "Common", "damage")
    MANA_CRYSTAL = ("Mana Crystal", 2, "Common", 5,
                    "Permanent: +1 mana per turn")
    WISDOM_RING = ("Ring of Wisdom", 4, "Rare", 4,
                   "Permanent: Draw an extra card each turn")


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power in ("dragon", 7):
            return CreatureCard(*Arg.FIRE_DRAGON.value)
        elif name_or_power in ("goblin", 2):
            return CreatureCard(*Arg.GOBLIN.value)
        return random.choice((
            CreatureCard(*Arg.FIRE_DRAGON.value),
            CreatureCard(*Arg.GOBLIN.value)
        ))

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power in ("fireball", 4):
            return SpellCard(*Arg.FIREBALL.value)
        elif name_or_power in ("lightning bolt", 3):
            return SpellCard(*Arg.LIGHTNING.value)
        return random.choice((
            SpellCard(*Arg.FIREBALL.value),
            SpellCard(*Arg.LIGHTNING.value)
        ))

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power in ("mana_crystal", 5):
            return ArtifactCard(*Arg.MANA_CRYSTAL.value)
        elif name_or_power in ("wisdom_ring", 4):
            return ArtifactCard(*Arg.WISDOM_RING.value)
        return random.choice((
            ArtifactCard(*Arg.MANA_CRYSTAL.value),
            ArtifactCard(*Arg.WISDOM_RING.value)
        ))

    def create_themed_deck(self, size: int) -> dict:
        deck = Deck()
        for _ in range(size):
            card_type = random.choice(['creature', 'spell', 'artifact'])
            if card_type == 'creature':
                deck.add_card(self.create_creature())
            elif card_type == 'spell':
                deck.add_card(self.create_spell())
            else:
                deck.add_card(self.create_artifact())
        deck.shuffle()
        return {
            'factory': 'FantasyCardFactory',
            'deck': deck,
            'deck_size': size,
            'deck_stats': deck.get_deck_stats()
        }

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_crystal']
        }
