players = ["John Smith", "Sarah Jones", "Mike Brown", "Lisa Chen", "Tom Wilson"]
match_scores = [
    [2, 3, 1],    # John's scores
    [4, 2, 9],    # Sarah's scores
    [0, 1, 2],    # Mike's scores
    [3, 3, 3],    # Lisa's scores
    [2, 2, 0]     # Tom's scores
]


def calcStats(players, match_scores):
    count = 0
    results = []

    print("\n")
    for i in players:
        total_goals = 0
        for j in match_scores[count]:
            total_goals += j
        print(i, "has scored a total of", total_goals, "total goals")
        results.append(total_goals)
        count += 1
    count = 0

    biggestValueName = ""
    biggestValue = results[0]

    for i in results:
        if i > biggestValue:
            biggestValue = i
            biggestValueName = players[count]
        count += 1

    print("\n")
    print(biggestValueName, "scored the most amount of goals with", biggestValue, "total goals")

    count = 0
    for i in match_scores:
        total_goals = 0
        total_player_matches = len(match_scores) * len(match_scores[0])
        for j in match_scores[count]:
            total_goals += j


        count += 1
        print("Average goal:", total_goals / total_player_matches)

calcStats(players, match_scores)
