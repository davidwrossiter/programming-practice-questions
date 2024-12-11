def  calc(info):
    output={}
    average=0
    length=0
    highest=0
    for i in info.keys():
        total=0
        for j in info[i]:
            average+=j
            total +=j
            length += 1
        output[i+" score total"] = total
        if total>highest:
            highest=total
            best=i
    output["bestScorer"]=best + " with a total score of " + str(highest)
    output["overallPerformance"]=round(average/length, 2)
    return output

stuff={
    "John Smith":[2, 3, 1],
    "Sarah Jones":[4, 2, 3],
    "Mike Brown":[0, 1, 2],
    "Lisa Chen":[3, 3, 3],
    "Tom Wilson":[2, 2, 0]
}

out=calc(stuff)
print(out)