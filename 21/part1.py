#!/usr/bin/python

import itertools as it

def cheapest_victory():
    weapons = [{"name": "dagger", "cost": 8, "damage": 4, "armour": 0},
              {"name": "shortsword", "cost": 10, "damage": 5, "armour": 0},
              {"name": "warhammer", "cost": 25, "damage": 6, "armour": 0},
              {"name": "longsword", "cost": 40, "damage": 7, "armour": 0},
              {"name": "greataxe", "cost": 74, "damage": 8, "armour": 0}]
    
    armours = [{"name": "leather", "cost": 13, "damage": 0, "armour": 1},
              {"name": "chainmail", "cost": 31, "damage": 0, "armour": 2},
              {"name": "splintmail", "cost": 53, "damage": 0, "armour": 3},
              {"name": "bandedmail", "cost": 75, "damage": 0, "armour": 5},
              {"name": "platemail", "cost": 102, "damage": 0, "armour": 5},
              {"name": "-NONE-", "cost": 0, "damage": 0, "armour": 0}]
    
    rings  = [{"name": "damage +1", "cost": 25, "damage": 1, "armour": 0},
              {"name": "damage +2", "cost": 50, "damage": 2, "armour": 0},
              {"name": "damage +3", "cost": 100, "damage": 3, "armour": 0},
              {"name": "defence +1", "cost": 20, "damage": 0, "armour": 1},
              {"name": "defence +2", "cost": 40, "damage": 0, "armour": 2},
              {"name": "defence +3", "cost": 80, "damage": 0, "armour": 3},
              {"name": "-NONE-", "cost": 0, "damage": 0, "armour": 0},
              {"name": "-NONE-", "cost": 0, "damage": 0, "armour": 0}]
              

    cheapest_victory = 10000

    for weapon, armour, worn_rings in it.product(weapons, armours, it.combinations(rings, 2)):
        cost = 0
        player = {"hp": 100}

        player["damage"] = weapon["damage"]
        cost += weapon["cost"]

        player["armour"] = armour["armour"]
        cost += armour["cost"]

        for ring in worn_rings:
            player["damage"] += ring["damage"]
            player["armour"] += ring["armour"]
            cost += ring["cost"]

        enemy = {"hp": 104, "damage": 8, "armour": 1}

        if player_win(player, enemy):
            if cost < cheapest_victory:
                cheapest_victory = cost

    return cheapest_victory

def player_win(player, enemy):
    while True:
        enemy["hp"] -= resolve_encounter(player["damage"], enemy["armour"])
        if enemy["hp"] <= 0:
            return True
        player["hp"] -= resolve_encounter(enemy["damage"], player["armour"])
        if player["hp"] <= 0:
            return False

def resolve_encounter(attacking_damage, defending_armour):
    return max(1, attacking_damage - defending_armour)


if __name__=="__main__":
    print cheapest_victory()
