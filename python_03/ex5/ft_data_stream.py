import random
import typing


def gen_event(players: list, actions: list) -> typing.Generator:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events: list) -> typing.Generator:
    while events:
        event_index = random.randrange(len(events))
        yield events.pop(event_index)


if __name__ == "__main__":
    players = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grup", "run",
               "move", "climb", "swim", "released"]
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        name, action = next(gen_event(players, actions))
        print(f"Event {i}: Player {name} did action {action}")
    print()
    events = []
    for i in range(10):
        events.append(next(gen_event(players, actions)))
    print(f"Built list of 10 events: {events}")
    print()
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")
