import random
import typing


def gen_event(players: list, actions: list) -> typing.Generator:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


if __name__ == "__main__":
    players = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grup", "run",
               "move", "climb", "swim", "released"]
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        name, action = next(gen_event(players, actions))
        print(f"Event {i}: Player {name} did action {action}")
    events = []
    for i in range(10):
        events.append(next(gen_event(players, actions)))
    print(f"Built list of 10 events: {events}")
