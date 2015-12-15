#!/usr/bin/python

import itertools
import re 

def bake_cookie(input_string):

    ingredients = {}
    ing_re = re.compile("(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)")

    for row in input_string.split("\n"):
        if row == "":
            continue

        groups = ing_re.match(row).groups()
        ingredients[groups[0]] = {"capacity": int(groups[1]),
                                  "durability": int(groups[2]),
                                  "flavour": int(groups[3]),
                                  "texture": int(groups[4]),
                                  "calories": int(groups[5])}
    

   
    recipe = {}
    for ingredient in ingredients.keys():
        recipe[ingredient] = 1

    for spoonful in range(100-4):
        add_spoonful(recipe, ingredients)

    return score_cookie_recipe(recipe, ingredients)

def add_spoonful(cookie_recipe, ingredients):
    
    best_score = 0
    ingredient_to_add = "Love"

    for ingredient in ingredients.keys():
        cookie_recipe[ingredient] += 1
        score = score_cookie_recipe(cookie_recipe, ingredients)
        cookie_recipe[ingredient] -= 1

        if score > best_score:
            best_score = score
            ingredient_to_add = ingredient

    cookie_recipe[ingredient_to_add] += 1

def score_cookie_recipe(cookie_recipe, ingredients):

    ing_scores = {"capacity": 0, "durability": 0, "flavour": 0, "texture": 0}

    for ingredient, quantity in cookie_recipe.items():
        for quality in ing_scores.keys():
            ing_scores[quality] += quantity*ingredients[ingredient][quality]

    for quality in ing_scores.keys():
        ing_scores[quality] = max(0, ing_scores[quality])
    return reduce(lambda a, b: a*b, ing_scores.values())

if __name__=="__main__":

    input_string = open("input.txt").read()

    print bake_cookie(input_string)
