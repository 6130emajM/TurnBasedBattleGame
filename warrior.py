from character import Character  # ✅ Correct import

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)

from character import Character

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=18)

    def special_ability(self, opponent):
        """Warrior executes a heavy attack"""
        damage = self.attack_power + 5
        opponent.health -= damage
        print(f"{self.name} performs a heavy attack on {opponent.name} for {damage} damage!")
