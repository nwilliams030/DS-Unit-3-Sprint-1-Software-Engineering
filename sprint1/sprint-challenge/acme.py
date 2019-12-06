"""
Parts 1-3 of Unit 3 sprint challenge.

Creating classes to organize inventory and do cool stuff.
"""

# Part 1 & 2:
from random import randint
from numpy import random

class Product():
    """ Class that represents products & their charachteristics """
    def __init__(self, name, price=10, weight=20, flammibility=0.5,
    identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammibility = flammibility
        self.identifier = identifier

    def stealability(self):
        val_stealish = self.price / self.weight
        if val_stealish < 0.5:
            return print('Not so stealable.')
        elif val_stealish >= 0.5 and val_stealish < 1.0:
            return print('Kinda stealable...')
        else:
            return print('Very Stealable!!')

    def explode(self):
        exp_factor = self.flammibility * self.weight
        if exp_factor < 10:
            return print('...fizzle')
        elif exp_factor >= 10 and exp_factor < 50:
            return print('...boom!')
        else:
            return print('..BABOOM!!!')

# Part 3:
class BoxingGlove(Product):
    """ Creating a class that represents the charachteristics and actions
    of our boxing glove product.
    """
    def __init__(
        self,
        name,
        price=10,
        weight=10,
        flamibility=0.5,
        identifier=randint(1000000, 9999999)
    ):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammibility = flamibility
        self.identifier = identifier

    def explode(self):
        return print("... It's a glove.")

    def punch(self):
        if self.weight < 5:
            return print('That tickles.')
        elif self.weight >= 5 and self.weight < 15:
            return print('Hey, that hurt!')
        else:
            return print("OUCH!!")
