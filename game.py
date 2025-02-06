from warrior import Warrior
from archer import Archer
from mage import Mage
from paladin import Paladin
from evil_wizard import EvilWizard

def main():
    print("Choose your class:")
    print("1. Warrior ⚔️")
    print("2. Archer 🏹")
    print("3. Mage 🔮")
    print("4. Paladin 🛡️")

    choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if choice == "1":
        player = Warrior(name)
    elif choice == "2":
        player = Archer(name)
    elif choice == "3":
        player = Mage(name)
    elif choice == "4":
        player = Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        player = Warrior(name)

    wizard = EvilWizard()  # ✅ FIXED: No arguments needed
    battle(player, wizard)

def battle(player, wizard):
    while player.health > 0 and wizard.health > 0:
        print("\nChoose an action:")
        print("1. Attack")
        print("2. Special Ability")
        print("3. Heal")
        
        action = input("Enter action: ")
        
        if action == "1":
            player.attack(wizard)
        elif action == "2":
            if hasattr(player, "special_ability"):  # ✅ Ensure player has a special ability
                player.special_ability(wizard)
            else:
                print("Your class does not have a special ability!")
        elif action == "3":
            player.heal()
        else:
            print("Invalid action, skipping turn.")

        if wizard.health > 0:
            wizard.special_ability(player)  # ✅ Wizard always attacks with dark magic
            wizard.regenerate()

    if player.health > 0:
        print(f"\n{player.name} has defeated the Evil Wizard! 🎉")
    else:
        print("\nThe Evil Wizard has won... 💀")

if __name__ == "__main__":
    main()

