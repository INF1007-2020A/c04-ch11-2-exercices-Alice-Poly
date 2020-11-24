"""
Chapitre 11.3

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	UNARMED_POWER = 20

	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self):
		return self.__name

	@classmethod
	def make_unarmed(cls):
		return cls("Unarmed", cls.UNARMED_POWER, 1)


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, name, max_hp, attack, defense, level):
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = None
		self.hp = max_hp
	
	@property
	def name(self):
		return self.__name

	@property
	def weapon(self):
		return self.__weapon

	@weapon.setter
	def weapon(self, val):
		if val is None:
			val = Weapon.make_unarmed()
		if val.min_level > self.level:
			raise ValueError(Weapon)
		self.__weapon = val

	@property
	def hp(self):
		return self.__hp

	@hp.setter
	def hp(self, val):
		self.__hp = utils.clamp(val, 0, self.max_hp)

	def compute_damage(self, other):
		return Character.compute_damage_output(
			self.level,
			self.weapon.power,
			self.attack,
			other.defense,
			1/16,
			(0.85, 1.00)
		)

	@staticmethod
	def compute_damage_output(level, power, attack, defense, crit_chance, random_range):
		level_factor = (2 * level) / 5 + 2
		weapon_factor = power
		atk_def_factor = attack / defense
		critical = random.random() <= crit_chance
		modifier = (2 if critical else 1) * random.uniform(*random_range)
		damage = ((level_factor * weapon_factor * atk_def_factor) / 50 + 2) * modifier
		return int(round(damage)), critical

