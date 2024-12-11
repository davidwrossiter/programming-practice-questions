
# Question set three

A local sports club needs a program to calculate team statistics. Write a program that:

    1. Accepts the names of 5 players
    2. Records their goal scores for 3 matches
    Calculates and displays:
        - The total goals for each player
        - The player with the highest scoring total
        - The team average goals per match

Key requirements:

    Use a function to validate that goal scores are between 0 and 10
    Store player data in appropriate data structures
    Include suitable error messages

Example input:

```
players = ["John Smith", "Sarah Jones", "Mike Brown", "Lisa Chen", "Tom Wilson"]
match_scores = [
    [2, 3, 1],    # John's scores
    [4, 2, 3],    # Sarah's scores
    [0, 1, 2],    # Mike's scores
    [3, 3, 3],    # Lisa's scores
    [2, 2, 0]     # Tom's scores
]

calculate_statistics(players, match_scores)
```
