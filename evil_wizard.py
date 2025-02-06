from character import Character
import random

class EvilWizard(Character):  
    def __init__(self):
        super().__init__("Evil Wizard", 100, 15)  # ✅ No need for an argument

    def special_ability(self, opponent):
        """Dark magic attack"""
        damage = random.randint(10, 25)
        opponent.health -= damage
        print(f"The Evil Wizard casts a dark spell on {opponent.name} for {damage} damage!")

    def regenerate(self):
        """Regenerate health"""
        heal_amount = random.randint(5, 15)
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"The Evil Wizard regenerates {heal_amount} health!")


