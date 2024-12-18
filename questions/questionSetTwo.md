# Battle Royale Match Analyzer

For each match, you have:

    - Damage Dealt (0-5000)
    - Survival Time in minutes (0-25)
    - Eliminations (0-99)
    - Materials Used (0-999)

Calculate:

    - DPM (Damage Per Minute) = Total Damage / Survival Time
    - Efficiency Rating = (Eliminations * 100) / Materials Used
    - Combat Score = (DPM * 0.6) + (Efficiency Rating * 0.4)
    - Performance Tier based on Combat Score:
        ≥ 200: "Pro"
        ≥ 150: "Diamond"
        ≥ 100: "Gold"
        < 100: "Silver"
Example input: 
```py
match_data = {
    "damage": 2400,
    "survival_time": 18,
    "eliminations": 6,
    "materials": 450
}
```

Expected output: 
```py
{
    "dpm": 133.33,
    "efficiency_rating": 1.33,
    "combat_score": 80.53,
    "performance_tier": "Silver",
}
```
