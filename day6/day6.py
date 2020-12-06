f = open("input.txt", "r")
input = []

group = []

for x in f: 
    if x == "\n": 
        input.append(group)
        group = []
    else: 
        group.append(x.strip())

input.append(group)

f.close()

def getYesResponses(group): 
    yesResponses = set()
    for response in group: 
        for i in range(len(response)): 
            yesResponses.add(response[i])
    return len(yesResponses)

def getAllYesResponses(group): 
    yesResponses = {}
    for response in group: 
        for i in range(len(response)): 
            if response[i] in yesResponses: 
                yesResponses[response[i]] += 1
            else: 
                yesResponses[response[i]] = 1

    allYesResponses = 0
    for key, val in yesResponses.items(): 
        if val == len(group): 
            allYesResponses += 1

    return allYesResponses

def q1(input): 
    output = 0
    for group in input: 
        yesResponses = getYesResponses(group)
        output += yesResponses
    return output

def q2(input): 
    output = 0
    for group in input: 
        allYesResponses = getAllYesResponses(group)
        output += allYesResponses
    return output

print(q1(input))
print(q2(input))


    


