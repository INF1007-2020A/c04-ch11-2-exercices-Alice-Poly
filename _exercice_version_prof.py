"""
Chapitre 11.3
"""


import math
from inspect import *

from game import *


def simulate_battle():
	c1 = Character("Äpik", 500, 150, 70, 70)
	c2 = Character("Gämmör", 550, 100, 120, 60)
	c3 = Magician("Damn! That magic dude", 450, 100, 50, 150, 50, 65)

	c1.weapon = Weapon("BFG", 100, 69)
	c2.weapon = Weapon("Deku Stick", 120, 1)
	c3.spell = Spell("Big Chungus Power", 100, 35, 50)
	c3.weapon = Weapon("Slingshot", 80, 20)
	c3.using_magic = True

	#print(c3.compute_damage(c1))
	#print(Character.compute_damage_output)
	#print(Magician.compute_damage_output)
	#print(c3.compute_damage_output)

	turns = run_battle(c3, c1)
	print(f"The battle ended in {turns} turns.")


def main():
	simulate_battle()

if __name__ == "__main__":
	main()

