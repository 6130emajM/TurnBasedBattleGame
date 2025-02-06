from character import Character
import random

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=20)
        self.evading = False
    
    def quick_shot(self, opponent):
        damage = random.randint(15, 30)  # Randomized attack
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot on {opponent.name} for {damage} damage!")

    def evade(self):
        print(f"{self.name} prepares to evade the next attack!")
        self.evading = True  # This can be used in battle logic
from character import Character

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=12)

    def special_ability(self, opponent):
        """Archer performs a double shot"""
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} fires a double shot at {opponent.name} for {damage} damage!")
