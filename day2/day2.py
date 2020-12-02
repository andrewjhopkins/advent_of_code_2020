f = open("input.txt", "r")
input = []

for x in f: 
    x = x.strip()
    if len(x) > 0: 
        passwordSet = x.split(" ")
        input.append(passwordSet)
f.close()

# frequency policy
def getValidPasswordsByFrequency(input): 
    valid = 0
    for i in input: 
        minMax = i[0].split("-")
        targetCharacter = i[1].replace(":", "")
        password = i[2]
        if checkIfFrequencyValid(int(minMax[0]), int(minMax[1]), targetCharacter, password): 
            valid += 1
    return valid

def checkIfFrequencyValid(minCharacters, maxCharacters, targetCharacter, password): 
    counter = 0
    for i in range(len(password)): 
        if password[i] == targetCharacter: 
            counter += 1
    return counter >= minCharacters and counter <= maxCharacters

# position policy
def getValidPasswordsByPosition(input): 
    valid = 0
    for i in input: 
        minMax = i[0].split("-")
        targetCharacter = i[1].replace(":", "")
        password = i[2]
        if checkIfPositionValid(int(minMax[0]) - 1, int(minMax[1]) - 1, targetCharacter, password): 
            valid += 1
    return valid

def checkIfPositionValid(minPosition, maxPosition, targetCharacter, password): 
    targetFound = False
    if password[minPosition] == targetCharacter: 
        targetFound = True

    if password[maxPosition] == targetCharacter: 
        if targetFound: 
            return False
        else: 
            return True

    return targetFound



print(getValidPasswordsByFrequency(input))
print(getValidPasswordsByPosition(input))





