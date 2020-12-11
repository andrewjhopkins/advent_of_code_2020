from copy import deepcopy 

f = open("input.txt", "r")

input = []
for x in f: 
    input.append(int(x.strip()))

f.close()

def q1(input): 
    numbers = deepcopy(input)
    deviceAdapter = max(numbers) + 3
    diffs = {}
    numbers.append(deviceAdapter)
    numbers.sort()

    for i in range(len(numbers)): 
        if i == 0: 
            diff = abs(numbers[i] - 0)
        else: 
            diff = abs(numbers[i] - numbers[i - 1])
        if diff in diffs: 
            diffs[diff] += 1
        else: 
            diffs[diff] = 1

    return diffs[1] * diffs[3]

def q2(input): 
    numbers = deepcopy(input)

    dynamic = {0: 1}

    for number in sorted(numbers): 
        dynamic[number] = 0
        if number - 1 in dynamic: 
            dynamic[number] += dynamic[number - 1]
        if number - 2 in dynamic: 
            dynamic[number] += dynamic[number - 2]
        if number - 3 in dynamic: 
            dynamic[number] += dynamic[number - 3]

    return dynamic[max(numbers)]


print(q1(input))
print(q2(input))
