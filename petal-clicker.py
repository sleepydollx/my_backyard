import time

UPGRADES = [
    {"name": "Better Finger",   "base_cost": 10,  "effect_type": "per_click",  "effect_value": 1, "owned": 0},
    {"name": "Tiny Helper",     "base_cost": 25,  "effect_type": "per_second", "effect_value": 1, "owned": 0},
    {"name": "Power Glove",     "base_cost": 100, "effect_type": "per_click",  "effect_value": 5, "owned": 0},
    {"name": "Petal Factory",   "base_cost": 250, "effect_type": "per_second", "effect_value": 5, "owned": 0},
    {"name": "Golden Cursor",   "base_cost": 1000, "effect_type": "per_click", "effect_value": 20, "owned": 0},
]

COST_GROWTH_RATE = 1.15 
AUTO_TICK_SECONDS = 1.0

import json
import os

def save_game(points, upgrades):
    data = {"points": points, "upgrades": upgrades}
    with open("savegame.json", "w") as f:
        json.dump(data, f)

def load_game():
    if os.path.exists("savegame.json"):
        with open("savegame.json") as f:
            data = json.load(f)
        # Restore upgrades from saved state
        for i, upgrade_data in enumerate(data["upgrades"]):
            UPGRADES[i]["owned"] = upgrade_data["owned"]
        return data["points"]
    return 0

def upgrade_current_cost(upgrade):
    return round(upgrade["base_cost"] * (COST_GROWTH_RATE ** upgrade["owned"]))


def calculate_totals():
    per_click = 1
    per_second = 0

    for upgrade in UPGRADES:
        total_effect = upgrade["effect_value"] * upgrade["owned"]
        if upgrade["effect_type"] == "per_click":
            per_click += total_effect
        elif upgrade["effect_type"] == "per_second":
            per_second += total_effect

    return per_click, per_second


def print_status(points, per_click, per_second):
    print(f"\n🌷 Points: {points}   |   +{per_click} per click   |   +{per_second}/sec")


def print_shop():
    print("\nShop:")
    for i, upgrade in enumerate(UPGRADES, start=1):
        cost = upgrade_current_cost(upgrade)
        print(f"  {i}) {upgrade['name']:<14} cost: {cost:<6} owned: {upgrade['owned']}")


def buy_upgrade(points, choice):
    index = choice - 1
    if index < 0 or index >= len(UPGRADES):
        print("That's not a valid upgrade number.")
        return points

    upgrade = UPGRADES[index]
    cost = upgrade_current_cost(upgrade)

    if points < cost:
        print(f"Not enough points! You need {cost}, you have {points}.")
        return points

    points -= cost
    upgrade["owned"] += 1
    print(f"Bought {upgrade['name']}! ({upgrade['owned']} owned now)")
    return points


def main():
    print("=" * 42)
    print("       🌷  PETAL CLICKER  🌷")
    print("=" * 42)
    print("Press Enter to click. Type 's' to open the shop.")
    print("Type 'q' to quit.\n")

    points = 0
    last_tick = time.time()

    while True:
        per_click, per_second = calculate_totals()

        now = time.time()
        elapsed = now - last_tick
        if elapsed >= AUTO_TICK_SECONDS and per_second > 0:
            ticks = int(elapsed // AUTO_TICK_SECONDS)
            points += ticks * per_second
            last_tick += ticks * AUTO_TICK_SECONDS

        print_status(points, per_click, per_second)
        action = input("[Enter]=click  s=shop  q=quit > ").strip().lower()

        if action == "":
            points += per_click
            print(f"Click! +{per_click} points")

        elif action == "s":
            print_shop()
            choice_input = input("Buy which number? (or press Enter to go back): ").strip()
            if choice_input.isdigit():
                points = buy_upgrade(points, int(choice_input))

        elif action == "q":
            break

        else:
            print("Didn't quite catch that — press Enter, 's', or 'q'.")

    print(f"\nFinal score: {points} points. Thanks for playing! ✿")


if __name__ == "__main__":
    main()
    
