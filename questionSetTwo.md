# Game Leaderboard Manager

You're developing a platform game where players complete levels and earn points. Write a function that analyzes player performance data and generates leaderboard statistics.

The function should take a list of player scores (each score represents points earned in a level, ranging from 0-1000) and calculate:

    1. The average score (to balance difficulty in future levels)
    2. The high score and low score
    3. Count how many players achieved "Pro Status" (score >= 750)
    4. Return these stats in a suitable format

Example input:

```js
level_scores = [340, 890, 670, 895, 960, 430, 755, 680]
```

Expected output:

```js
{
    "average_score": 702.5,
    "high_score": 960,
    "low_score": 340,
    "pro_players": 4
}
```
