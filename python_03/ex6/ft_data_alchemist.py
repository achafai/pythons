import random

print("=== Game Data Alchemist ===")
players: list = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]
print(f"Initial list of players: {players}")
print()
players_capitalized: list = [x.capitalize() for x in players]
print(f"New list with all names capitalized: {players_capitalized}")
print()
capitalized_players: list = [x for x in players if x == x.capitalize()]
print(f"New list of capitalizd names: {capitalized_players}")
print()
dictionary: dict = {x: random.randrange(1000) for x in players_capitalized}
print(f"Score dictionary: {dictionary}")
avrg: float = sum(dictionary.values()) / len(dictionary.values())
print(f"Score average is {avrg}")
new_dictionary: dict = {x: y for x, y in dictionary.items() if y > avrg}
print(f"High scores: {new_dictionary}")
