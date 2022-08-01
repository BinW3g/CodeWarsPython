# codewars challenge link
# https://www.codewars.com/kata/525c65e51bf619685c000059
import math


def cakes(recipe, available):
    highest_amount = 0
    for key in recipe.keys():
        if key not in available:
            return 0
        possible_amount = available[key]/recipe[key]
        if possible_amount < highest_amount or highest_amount == 0:
            highest_amount = possible_amount
    return math.floor(highest_amount)


if __name__ == '__main__':
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    print(cakes(recipe, available) == 2)

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    print(cakes(recipe, available) == 0)
