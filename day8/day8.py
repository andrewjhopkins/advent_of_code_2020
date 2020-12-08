f = open("input.txt", "r")
input = []
nopOrJmpIndex = []

for index, x in enumerate(f): 
    x = x.strip().split(" ")
    x[1] = int(x[1])

    if x[0] == "nop" or x[0] == "jmp": 
        nopOrJmpIndex.append(index)

    input.append(x)

f.close()

def q1(input): 
    cache = set()
    index = 0
    accumulator = 0

    while index not in cache and index < len(input): 
        cache.add(index)
        command = input[index][0]
        value = input[index][1]

        if command == "nop": 
            index += 1
        elif command == "acc": 
            accumulator += value
            index += 1
        elif command == "jmp": 
            index += value

    return (index >= len(input), accumulator)

def q2(input, nopOrJmpIndex): 
    for changeIndex in nopOrJmpIndex: 

        input[changeIndex][0] = "nop" if input[changeIndex][0] == "jmp" else "jmp"

        value = q1(input)

        if value[0] == True: 
            return value[1]

        input[changeIndex][0] = "nop" if input[changeIndex][0] == "jmp" else "jmp"

    return 0


print(q1(input))
print(q2(input, nopOrJmpIndex))

