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
    


    highest_score = 0
    for comb in itertools.combinations_with_replacement(ingredients.keys(), 100):
        recipe = {}
        for ing in ingredients:
            recipe[ing] = comb.count(ing)

        score = score_cookie_recipe(recipe, ingredients)
        calories = calculate_calories(recipe, ingredients)
        if score > highest_score and calories == 500:
            highest_score = score
 
    return highest_score

def calculate_calories(cookie_recipe, ingredients):
    calories = 0
    for ing in ingredients.keys():
        calories += ingredients[ing]["calories"]*cookie_recipe[ing]

    return calories

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
