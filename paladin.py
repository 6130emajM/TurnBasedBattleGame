from character import Character  # ✅ Correct import

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=12)

from character import Character

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=14)

    def special_ability(self, opponent):
        """Paladin smites the enemy with holy power and heals slightly"""
        damage = self.attack_power + 8
        self.health = min(self.max_health, self.health + 5)  # Heals a little
        opponent.health -= damage
        print(f"{self.name} smites {opponent.name} for {damage} damage and heals 5 HP!")
