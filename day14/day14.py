import copy

f = open("input.txt", "r")

mask = None
bits = []
iterations = []

for i, x in enumerate(f): 

    xSplit = x.strip().split("= ")
    if xSplit[0].strip() == "mask": 
        if mask is not None: 
            iterations.append((mask, bits))
        mask = list(xSplit[1])
        bits = []
    else: 
        x = x.strip()
        location = x[x.find("[")+1:x.find("]")]
        value = int(x.split("= ")[1])
        bits.append((location, value))

iterations.append((mask, bits))

f.close()


def intToBits(value): 
    bits = ["0"] * 36
    start = 0
    while((2 ** start) < value): 
        start += 1
    start -= 1

    for i in range(start, -1, -1): 
        if(value > 0 and (2 **i) <= value): 
            bits[i] = "1"
            value -= (2 ** i)

    bits.reverse()
    return bits

def q1(iteration): 
    memory = {}
    
    for iteration in iterations: 
        mask = iteration[0]
        bits = iteration[1]

        for bit in bits: 
            bitValue = list(bin(bit[1])[2:].zfill(36))
            for i, value in enumerate(mask): 
                if mask[i] != "X": 
                    bitValue[i] = mask[i]

            intValue = int("".join(bitValue), base=2)
            memory[bit[0]] = intValue

    output = 0
    for key, value in memory.items(): 
        output += value

    return output

def q2(iteration): 
    memory = {}
    for iteration in iterations: 
        mask = iteration[0]
        bits = iteration[1]
        
        bitAddresses = set()

        for bit in bits: 
            bitValue = list(bin(int(bit[0]))[2:].zfill(36))
            for i, value in enumerate(mask): 
                if mask[i] == "X": 
                    bitValue[i] = mask[i]
                elif mask[i] == "1": 
                    bitValue[i] = "1"

            bitAddresses.add("".join(bitValue))

            for i, value in enumerate(bitValue): 
                newAddresses = set()
                if mask[i] == "X": 
                    for key in bitAddresses:
                        copy = list(key)
                        copy[i] = "1"
                        newAddresses.add("".join(copy))

                        copy[i] = "0"
                        newAddresses.add("".join(copy))

                    bitAddresses = newAddresses

            for value in bitAddresses: 
                intValue = int(value, 2)
                memory[intValue] = bit[1]

    return sum(memory.values())



# print(q1(iterations))
print(q2(iterations))

