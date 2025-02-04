from character import Character
import random

class EvilWizard(Character):
    def __init__(self):
        super().__init__("Evil Wizard", health=150, attack_power=15)

    def regenerate(self):
        regen = random.randint(5, 10)
        self.health += regen
        print(f"{self.name} regenerates {regen} health! Current health: {self.health}")

    def dark_spell(self, opponent):
        damage = random.randint(20, 35)
        opponent.health -= damage
        print(f"{self.name} casts Dark Spell on {opponent.name} for {damage} damage!")