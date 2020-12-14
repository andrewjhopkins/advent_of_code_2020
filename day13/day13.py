f = open("input.txt", "r")

startTime = 0
busIds = []
for i, x in enumerate(f): 
    if i == 0: 
        startTime = int(x.strip())
    else: 
        ids = x.strip().split(",")
        for j in ids: 
            if j == "x": 
                busIds.append(j)
            else: 
                busIds.append(int(j))
f.close()

def q1(startTime, busIds): 
    minWaitTime = float("inf")
    minWaitId = None

    for busId in busIds: 
        if busId == "x": 
            continue
        minTimeAfterStart = (startTime - (startTime % busId)) + busId
        waitTime = minTimeAfterStart - startTime
        if waitTime < minWaitTime: 
            minWaitTime = waitTime
            minWaitId = busId

    return minWaitId * minWaitTime

def findT(start, counter, ids): 
    t = start
    found = True
    while(found): 
        t += counter
        found = False
        for i in range(len(ids)): 
            if ids[i] == "x": 
                continue
            tShift = t + i
            if(tShift % ids[i] != 0): 
                found = True
    return t
                


def q2(busIds): 
    start = 0
    counter = 1

    for i in range(1, len(busIds)): 
        if busIds[i] == "x": 
            continue
        else: 
            start = findT(start, counter, busIds[0:i+1])
            if i == 1: 
                counter = busIds[0] * busIds[1]
            else: 
                counter *= busIds[i]
    return start

print(q1(startTime, busIds))
print(q2(busIds))
