from character import Character  # ✅ Correct import

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=70, attack_power=25)

from character import Character  # ✅ Correct import

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)

    def special_ability(self, opponent):
        """Mage casts a powerful spell dealing extra damage"""
        damage = self.attack_power + 10  # Adjust as needed
        opponent.health -= damage
        print(f"{self.name} casts a spell on {opponent.name} for {damage} damage!")
