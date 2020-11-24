"""
Chapitre 11.3

Classes pour représenter un magicien et ses pouvoirs magiques.
"""


import random

import utils
from character import *


# TODO: Créer la classe Spell qui a les même propriétés que Weapon, mais avec un coût en MP pour l'utiliser
class Spell:
	"""
	Un sort dans le jeu.

	:param name: Le nom du sort
	:param power: Le niveau d'attaque
	:param mp_cost: Le coût en MP d'utilisation du sort
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	# TODO: __init__
	pass

# TODO: Déclarer la classe Magician qui étend la classe Character
class Magician:
	"""
	Un utilisateur de magie dans le jeu. Un magicien peut utiliser des sorts, mais peut aussi utiliser des armes physiques. Sa capacité à utiliser des sorts dépend 

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param max_mp: MP maximum
	:param attack: Le niveau d'attaque physique du personnage
	:param magic_attack: Le niveau d'attaque magique du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage

	:ivar using_magic: Détermine si le magicien tente d'utiliser sa magie dans un combat.
	"""

	def __init__(self, name, max_hp, max_mp, attack, magic_attack, defense, level):
		# TODO: Initialiser les attributs de Character
		# TODO: Initialiser le `magic_attack` avec le paramètre, le `max_mp` et `mp` de la même façon que `max_hp` et `hp`, `spell` à None et `using_magic` à False.
		pass

	@property
	def mp(self):
		return self.__mp

	@mp.setter
	def mp(self, val):
		self.__mp = utils.clamp(val, 0, self.max_hp)

	# TODO: Écrire les getter/setter pour la propriété `spell`.
	#       On peut affecter None.
	#       Si le niveau minimal d'un sort est supérieur au niveau du personnage, on lève ValueError.

	# TODO: Surcharger la méthode `compute_damage` 
	def compute_damage(self, other):
		# Si le magicien va utiliser sa magie (`will_use_spell()`):
			# Soustraire à son MP le coût du sort
			# Retourner le résultat du calcul de dégâts magiques
		# Sinon
			# Retourner le résultat du calcul de dégâts physiques
		pass

	def will_use_spell(self):
		return self.using_magic and self.spell is not None and self.mp >= self.spell.mp_cost

	def _compute_magical_damage(self, other):
		return Character.compute_damage_output(
			self.level + self.magic_attack,
			self.spell.power,
			1,
			1,
			1/8,
			(0.85, 1.00)
		)

	def _compute_physical_damage(self, other):
		# TODO: Calculer le dommage physique exactement de la même façon que dans `Character`
		pass

