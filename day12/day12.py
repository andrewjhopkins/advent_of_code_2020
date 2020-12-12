f = open("testInput.txt", "r")

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
    currentDirection = "east"
    distance = { "east": 0, "west": 0, "north": 0, "south": 0 }
    waypointDistance = { "east": 10, "west": 0, "north": 1, "south": 0 }

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

print(q1(input))
print(q2(input))
