def analyzePerformance(stats):
    dpm = round(stats["damage"] / stats["timeAlive"],2)
    efficiency = round((stats["elims"] * 100) / stats["usage"],2)
    score = (dpm * 0.6) + (efficiency * 0.4)
    tier = "silver"
    if score >= 100:
        tier = "gold"
        if score >=150:
            tier = "diamond"
            if score >= 200:
                tier = "pro"
    return {
        "dpm":dpm,
        "efficiency":efficiency,
        "score":score,
        "tier":tier
    }

stats = analyzePerformance({
    "damage":2400,
    "timeAlive":18,
    "elims":6,
    "usage":450
})

print(stats)