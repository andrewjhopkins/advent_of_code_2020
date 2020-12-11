from copy import deepcopy

f = open("input.txt", "r")

input = []
for x in f: 
    row = list(x.strip())
    input.append(row)
f.close()

def printGrid(grid): 
    for row in grid: 
        print("\n")
        print(row)

def getNextState(c, r, grid, occupied, empty, occupiedTurnEmpty, emptyTurnOccupied): 
    occupiedCells  = 0
    cords = [(c - 1, r - 1), (c - 1, r), (c - 1, r + 1), (c, r - 1), (c, r + 1), (c + 1, r - 1), (c + 1, r), (c + 1, r + 1)]

    for cord in cords:
        if cord[0] >= 0 and cord[0] < len(grid) and cord[1] >= 0 and cord[1] < len(grid[c]): 
            if grid[cord[0]][cord[1]] == occupied or grid[cord[0]][cord[1]] == occupiedTurnEmpty: 
                occupiedCells += 1

    if occupiedCells == 0 and grid[c][r] == empty: 
        return emptyTurnOccupied
    if occupiedCells >= 4 and grid[c][r] == occupied: 
        return occupiedTurnEmpty

    return grid[c][r]

def getV2NextState(c, r, grid, occupied, empty, occupiedTurnEmpty, emptyTurnOccupied): 
    occupiedCells  = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for direction in directions:
        col = c + direction[0]
        row = r + direction[1]
        notFound = True

        while(notFound and col >= 0 and col < len(grid) and row >= 0 and row < len(grid[col])): 
            if grid[col][row] != ".": 
                notFound = False
                if grid[col][row] == occupied or grid[col][row] == occupiedTurnEmpty: 
                    occupiedCells += 1
            col += direction[0]
            row += direction[1]

    if occupiedCells == 0 and grid[c][r] == empty: 
        return emptyTurnOccupied
    if occupiedCells >= 5 and grid[c][r] == occupied: 
        return occupiedTurnEmpty

    return grid[c][r]



def q1(input, version): 
    grid = deepcopy(input)
    occupied = "#"
    empty = "L"
    emptyTurnOccupied = "1"
    occupiedTurnEmpty = "2"
    iterations = 0

    changes = True
    
    while(changes): 
        changes = False
        for c in range(len(grid)): 
            for r in range(len(grid[c])): 
                if version == "v1": 
                    nextState = getNextState(c, r, grid, occupied, empty, occupiedTurnEmpty, emptyTurnOccupied)
                    grid[c][r] = nextState
                if version == "v2": 
                    nextState = getV2NextState(c, r, grid, occupied, empty, occupiedTurnEmpty, emptyTurnOccupied)
                    grid[c][r] = nextState

        for c in range(len(grid)): 
            for r in range(len(grid[c])): 
                if grid[c][r] == emptyTurnOccupied: 
                    grid[c][r] = occupied
                    changes = True
                elif grid[c][r] == occupiedTurnEmpty: 
                    grid[c][r] = empty
                    changes = True
        iterations += 1
    
    output = 0
    for row in grid: 
        for cell in row: 
            if cell == occupied: 
                output += 1

    return output


print(q1(input, "v1"))
print(q1(input, "v2"))


