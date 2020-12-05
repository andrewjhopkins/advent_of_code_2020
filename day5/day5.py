
f = open("input.txt", "r")
input = []

for x in f: 
    input.append(x.strip())

f.close()

def getRow(ticket): 
    min, max = 0, 127
    for i in range(len(ticket) - 1): 
        midPoint = min + (max - min) // 2
        if ticket[i] == "B": 
            min = midPoint + 1
        else: 
            max = midPoint
    return min if ticket[-1] == "F" else max

def getColumn(ticket): 
    min, max = 0, 7
    for i in range(len(ticket) - 1): 
        midPoint = min + (max - min) // 2
        if ticket[i] == "R": 
            min = midPoint + 1
        else: 
            max = midPoint
    return min if ticket[-1] == "L" else max

def q1(input): 
    output = float("-inf")
    for i in range(len(input)): 
        row = getRow(input[i][:7])
        column = getColumn(input[i][7:])
        id = row * 8 + column
        if id > output: 
            output = id
    return output

def q2(input): 
    out = []
    for i in range(len(input)): 
        row = getRow(input[i][:7])
        column = getColumn(input[i][7:])
        id = row * 8 + column
        out.append(id)
    out.sort()

    missingSeats = []
    for i in range(1, len(out)): 
        if(out[i - 1] != out[i] - 1): 
            missingSeats.append(out[i] - 1)
    return missingSeats


print(q1(input))
print(q2(input))




