"""
Chapitre 11.3

Fonctions pour simuler un combat.
"""


import random

import utils
from character import *
from magician import *


def deal_damage(attacker, defender):
	# TODO: Obtenir l'arme utilisée.
	#       Si l'attaquant est un magicien et que `Magician.will_use_spell()` donne vrai, il utilise sa magie.
	#       Sinon il utilise son arme physique.
	weapon_used = None
	damage, crit = attacker.compute_damage(defender)
	defender.hp -= damage
	print(f"  {attacker.name} used {weapon_used.name}")
	if crit:
		print("    Critical hit!")
	print(f"    {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	attacker = c1
	defender = c2
	turns = 1
	print(f"{attacker.name} would like to battle.")
	print(f"{defender.name} accepted!")
	while True:
		deal_damage(attacker, defender)
		if defender.hp == 0:
			print(f"  {defender.name } is sleeping with the fishes.")
			break
		turns += 1
		attacker, defender = defender, attacker
	return turns
