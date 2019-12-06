"""
Part 4 of Unit 3 sprint challenge.

Creating a report for our inventory.
"""

from acme import Product
from random import randint, sample, uniform
from numpy import random


# Defining the makeup of the random names for products
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


# Making the products
def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        # build the name of the product
        adj = sample(ADJECTIVES, 1)
        noun = sample(NOUNS, 1)
        name = adj[0] + ' ' + noun[0]

        price = round(uniform(5.00, 1938.67), 2)
        weight = round(uniform(0.5, 600.5), 2)
        flammibility = round(uniform(0.0, 2.5), 6)

        products.append(Product(name, price, weight, flammibility))
    return products


def generate_report(products):
    # Create empty lists to populate.
    names = []
    prices = []
    weights = []
    flames = []
    # Loop over products list
    for x in products:
        names.append(x.name)
        prices.append(x.price)
        weights.append(x.weight)
        flames.append(x.flammibility)

    print(f'Unique product names: {len(set(names))}')
    print(f'Average price: ${round(sum(prices) / len(prices),2)}')
    print(f'Average weight: {round(sum(weights) / len(weights), 2)} ')
    print(f'Average flammability: {round(sum(flames) / len(flames), 2)}')
    return names, prices, weights, flames


if __name__ == '__main__':
    generate_report(generate_products())
