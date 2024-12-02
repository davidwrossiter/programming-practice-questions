def dealWithScores(scores):
    info={
        "average":0,
        "highest":0,
        "lowest":100,
        "passes":0
    }
    for i in scores:
        info["average"] += i
        if i > info["highest"]:
            info["highest"] = i
        elif i < info["lowest"]:
            info["lowest"] = i
        if i >= 50:
            info["passes"] += 1
    info["average"]/=len(scores)
    return info

stuff = dealWithScores([45, 78, 92, 33, 65, 89, 54, 23])

print(stuff)