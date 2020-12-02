f = open("input.txt", "r")
input = []

for x in f: 
    x = x.strip()
    if len(x) > 0: 
        input.append(int(x))

f.close()

target = 2020

# 2 entries that equal 2020
def twoEntries(input): 
    entries = set()
    for i in input: 
        if target - i in entries: 
            return (target - i) * i
        else: 
            entries.add(i)

# 3 entries that equal 2020
def threeEntries(input):
    for i in range(len(input)): 
        num1 = input[i]
        entries = set()
        for j in range(i + 1, len(input)): 
            num2 = input[j]
            if target - num1 - input[j] in entries: 
                return num1 * num2 * (target - num1 - num2)
            else:
                entries.add(num2)

print(twoEntries(input))
print(threeEntries(input))











