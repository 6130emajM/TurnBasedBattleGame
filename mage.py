from character import Character

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.shielded = False

    def fireball(self, opponent):
        damage = 40
        opponent.health -= damage
        print(f"{self.name} casts Fireball on {opponent.name} for {damage} damage!")

    def mana_shield(self):
        print(f"{self.name} activates Mana Shield, reducing incoming damage for the next turn!")
        self.shielded = True  # This can be used in battle logic