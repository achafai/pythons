import random


def gen_player_achievements(achievements: list) -> set:
    achievements_number = random.randrange(1, len(achievements) + 1)
    return set(random.choices(population=achievements, k=achievements_number))


if __name__ == "__main__":
    achievements = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
    ]
    print("=== Achievement Tracker System ===")
    print()
    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    print(f"All distanct achievements: {set(achievements)}")
    print()
    print("Common achievements: ", end="")
    print(set.intersection(alice, bob, charlie, dylan))
    print()
    print("Only Alice has: ", end="")
    print(alice.difference(bob, charlie, dylan))
    print("Only Bob has: ", end="")
    print(bob.difference(alice, charlie, dylan))
    print("Only Charlie has: ", end="")
    print(charlie.difference(bob, alice, dylan))
    print("Only Dylan has: ", end="")
    print(dylan.difference(bob, charlie, alice))
    print()
    print(f"Alice is missing {set(achievements).difference(alice)}")
    print(f"Bob is missing {set(achievements).difference(bob)}")
    print(f"Charlie is missing {set(achievements).difference(charlie)}")
    print(f"Dylan is missing {set(achievements).difference(dylan)}")
