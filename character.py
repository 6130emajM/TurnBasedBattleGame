# character.property
import random

class character:
    def __init__(self, name, health, attack_power):
        self.name _ name
        self.health = health
        self.attack_power = attack_powerself.max_health = health
        
        def attack(self, opponent):
            """Attack with random damage"""
            damage = random.randint(self.attack_power - 5, self.attack_power + 5)
            opponent.health -= damage
            print(f{self.name}" attacks {opponent.name} for {damage} damage!")
            
            if opponent,health <= 0:
                print(f"{opponent.name} has been defeated!")
                
                def heal(self):
                    """Heal the character"""
                    heal_amount = random.randint(10, 200
                                                 self.health = min(self.max_health, self.health + heal_amount)
                                                 print(f"{self.name} heals for {heal_amount}. Current health: {self.health}/{self.max_health}") 
                                                
                                                def display_stats(self):
                                                    """Show character stats"""
                                                    print(f"{self.name} - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
            