#!/usr/bin/python

possibilities = 0
depth = 0

def play_game(player, boss, spells, effects=[]):

    global possibilities, depth
    depth += 1
    possibilities += 1

    lowest_cost = None
    lowest_moves = None

    # Apply active effects
    player["armour"] = 0
    for effect in effects:
        player, boss = effect["action"](player, boss)
        effect["duration"] -= 1
    effects = filter(lambda effect: effect["duration"] > 0, effects)

    # If boss is dead
    if boss["hp"] <= 0:
        return 0, []

    # Try all the possible moves
    for move in available_moves(player, spells, effects):
        # Create copies of player, boss, and effects
        move_player = player.copy()
        move_boss = boss.copy()
        move_effects = []
        for effect in effects:
            move_effects.append(effect.copy())

        # Take move
        move_player["mana"] -= move["cost"]
        if move["is_effect"]:
            move_effects.append({"name": move["name"], "action": move["action"], "duration": move["duration"]})
        else:
            move_player, move_boss = move["action"](move_player, move_boss)

        # Check if boss is dead
        if move_boss["hp"] <= 0:
            if lowest_cost is None:
                lowest_cost = move["cost"]
                lowest_moves = [move["name"]]
            elif move["cost"] < lowest_cost:
                lowest_cost = move["cost"]
                lowest_moves = [move["name"]]
            continue

        # Reapply active effects
        move_player["armour"] = 0
        for effect in move_effects:
            move_player, move_boss = effect["action"](move_player, move_boss)
            effect["duration"] -= 1
        move_effects = filter(lambda effect: effect["duration"] > 0, move_effects)
        
        # Check boss still alive
        if move_boss["hp"] <= 0:
            if lowest_cost is None:
                lowest_cost = move["cost"]
                lowest_moves = [move["name"]]
            elif move["cost"] < lowest_cost:
                lowest_cost = move["cost"]
                lowest_moves = [move["name"]]
            continue

        # Boss makes move
        move_player["hp"] -= max(1, move_boss["damage"] - move_player["armour"])
        
        # Check player still alive
        if move_player["hp"] <= 0:
            continue

        cost, moves = play_game(move_player, move_boss, spells, move_effects)
        if cost is not None:
            if lowest_cost is None:
                lowest_cost = move["cost"] + cost
                lowest_moves = [move["name"]] + moves
            elif cost + move["cost"] < lowest_cost:
                lowest_cost = move["cost"] + cost
                lowest_moves = [move["name"]] + moves

    depth -= 1
    return lowest_cost, lowest_moves

def available_moves(player, spells, effects):
    moves = filter(lambda spell: spell["cost"] <= player["mana"], spells)
    moves = filter(lambda spell: effect_is_not_active(spell, effects), moves)
    return moves

def effect_is_not_active(spell, effects):
    for effect in effects:
        if spell["name"] == effect["name"]:
            return False
    else:
        return True

def missile_action(player, boss):
    player, boss = player.copy(), boss.copy()
    boss["hp"] -= 4
    return player, boss

def drain_action(player, boss):
    player, boss = player.copy(), boss.copy()
    player["hp"] += 2
    boss["hp"] -= 2
    return player, boss

def poison_action(player, boss):
    player, boss = player.copy(), boss.copy()
    boss["hp"] -= 3
    return player, boss

def shield_action(player, boss):
    player, boss = player.copy(), boss.copy()
    player["armour"] = 7
    return player, boss

def recharge_action(player, boss):
    player, boss = player.copy(), boss.copy()
    player["mana"] += 101
    return player, boss

if __name__=="__main__":
    
    player = {"hp": 50, "mana": 500, "armour": 0}
    boss = {"hp": 71, "damage": 10}

    spells = [{"name": "missile", "cost": 53, "action": missile_action, "is_effect": False},
              {"name": "drain", "cost": 73, "action": drain_action, "is_effect": False},
              {"name": "poison", "cost": 173, "action": poison_action, "is_effect": True, "duration": 6},
              {"name": "shield", "cost": 113, "action": shield_action, "is_effect": True, "duration": 6},
              {"name": "recharge", "cost": 229, "action": recharge_action, "is_effect": True, "duration": 5}]

    cost, moves = play_game(player, boss, spells)
    print cost
