import sys


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print(f"No scores provided. Usage: python3 {sys.argv[0]}", end=" ")
        print("<score1> <score2> ...")
    scores = []
    for element in sys.argv[1:]:
        try:
            scores.append(int(element))
        except ValueError:
            print(f"Invalid input: '{element}'")
    if len(scores) < 1:
        print(f"No scores provided. Usage: python3 {sys.argv[0]}", end=" ")
        print("<score1> <score2> ...")
    else:
        total_players = len(scores)
        total_score = sum(scores)
        average_score = total_score/total_players
        high_score = max(scores)
        low_score = min(scores)
        score_range = high_score - low_score
        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {score_range}")
