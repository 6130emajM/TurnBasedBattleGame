from character import Character

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=25)
        self.shielded = False

    def holy_strike(self, opponent):
        damage = 30
        opponent.health -= damage
        print(f"{self.name} performs Holy Strike on {opponent.name} for {damage} damage!")

    def divine_shield(self):
        print(f"{self.name} casts Divine Shield, blocking the next attack!")
        self.shielded = True  # This can be used in battle logic