#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  min_batch_values = []
  if set(recipe.keys()).issubset(set(ingredients.keys())):
    for ingredient in ingredients:
      min_batch_values.append(ingredients[ingredient]//recipe[ingredient])
  else:
    return 0
  return min(min_batch_values)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))