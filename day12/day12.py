from collections import deque

f = open("input.txt", "r")

input = []
for x in f: 
    input.append(x.strip())
f.close()

def getNextDirection(currentDirection, units, action): 
    directions = ["north", "east", "south", "west"]
    index = directions.index(currentDirection)
    moves = units // 90

    direction = 1 if action == "R" else -1

    for i in range(moves): 
        index += direction
        if index > len(directions) - 1: 
            index = 0
        if index < 0: 
            index = len(directions) - 1

    return directions[index]

def getWayPointDistance(waypointDistance, units, action): 
    moves = units // 90
    direction = 1 if action == "R" else -1

    directions = [0, 0, 0, 0]
    if waypointDistance[0] > 0: 
        directions[0] = abs(waypointDistance[0])
    if waypointDistance[0] < 0: 
        directions[2] = abs(waypointDistance[0])
    if waypointDistance[1] > 0: 
        directions[1] = abs(waypointDistance[1])
    if waypointDistance[1] < 0: 
        directions[3] = abs(waypointDistance[1])

    for i in range(moves): 
        directions = deque(directions)
        directions.rotate(direction)

    for i in range(len(directions)): 
        if directions[i] > 0: 
            if i == 0: 
                waypointDistance[0] = directions[i]
            elif i == 2: 
                waypointDistance[0] = directions[i] * -1
            elif i == 1: 
                waypointDistance[1] = directions[i]
            elif i == 3: 
                waypointDistance[1] = directions[i] * -1

    return waypointDistance

def getManhattanDistance(distances): 
    ns = abs(distances["north"] - distances["south"])
    ew = abs(distances["east"] - distances["west"])

    return (ns + ew)

def q1(input): 
    currentDirection = "east"
    distance = { "east": 0, "west": 0, "north": 0, "south": 0 }

    for direction in input: 
        action = direction[0]
        units = int(direction[1:])

        if action == "N": 
            distance["north"] += units
        elif action == "S": 
            distance["south"] += units
        elif action == "E": 
            distance["east"] += units
        elif action == "W": 
            distance["west"] += units
        elif action == "F": 
            distance[currentDirection] += units
        else: 
            currentDirection = getNextDirection(currentDirection, units, action)

    return getManhattanDistance(distance)

def q2(input): 
    # index 0 north(+), south(-)
    # index 1 east(+), west(-)
    shipDistance = [0, 0]
    waypointDistance = [1, 10]

    for direction in input: 
        action = direction[0]
        units = int(direction[1:])

        if action == "N": 
            waypointDistance[0] += units
        elif action == "S": 
            waypointDistance[0] -= units
        elif action == "E": 
            waypointDistance[1] += units
        elif action == "W": 
            waypointDistance[1] -= units
        elif action == "F": 
            for i in range(len(shipDistance)): 
                shipDistance[i] = shipDistance[i] + (waypointDistance[i] * units)
        else: 
            waypointDistance = getWayPointDistance(waypointDistance, units, action)

    return abs(shipDistance[0] + shipDistance[1])

print(q1(input))
print(q2(input))
