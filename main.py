from character import Hero, Villain
from utils import get_random_from_files

hero_name = get_random_from_files(r"data/heroes.txt")
hero_weapon = get_random_from_files(r"data/weapons.txt")
villain_name = get_random_from_files(r"data/villains.txt")
villain_weapon = get_random_from_files(r"data/weapons.txt")

Hero = Hero(hero_name, hero_weapon)
Villain = Villain(villain_name, villain_weapon)

print("BATTLE BEGINS!")

print(f"Hero: {Hero.name} | HP: {Hero.hp} | Weapon: {Hero.weapon}")
print(f"Villain: {Villain.name} | HP: {Villain.hp} | Weapon: {Villain.weapon}")

round_number = 1

while Hero.is_alive() and Villain.is_alive():
    print(f"\n--- Round {round_number} ---")
    Hero.attack(Villain)

    if not Villain.is_alive():
        break

    Villain.attack(Hero)

    round_number = round_number + 1

print("\n--- BATTLE ENDS ---")

if Hero.is_alive():
    print("Hero saves the day!")
else:
    print("Dark side wins!")
