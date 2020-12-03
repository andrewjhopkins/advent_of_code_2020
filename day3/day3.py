f = open("input.txt", "r")
input = []

for x in f: 
    input.append(list(x.strip()))
f.close()

def findAmountOfTrees(grid, rightSlope, downSlope): 
    count = 0
    right = 0
    for i in range(0, len(grid), downSlope): 
        if right > len(grid[i]) - 1: 
            right -= len(grid[i])
        if grid[i][right] == "#": 
            count += 1
        right += rightSlope
    return count



print(findAmountOfTrees(input, 3, 1))

outputSum = 1
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

for slope in slopes: 
    outputSum *= findAmountOfTrees(input, slope[0], slope[1])

print(outputSum)




