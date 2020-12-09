f = open("input.txt", "r")
input = []

for x in f: 
    input.append(int(x.strip()))

f.close()

def findBadNumber(input, preamble): 
    numbers = {}
    startIndex = 0

    for i in range(preamble, len(input)): 
        if not twoSum(input[i], input[startIndex:i]): 
            return (input[i], i)
        startIndex += 1

def twoSum(target, numbers): 
    dic = set()
    for i in range(len(numbers)): 
        num = target - numbers[i]
        if num in dic: 
            return True
        else: 
            dic.add(numbers[i])
    return False

def findContiguousSum(numbers, target, targetIndex): 
    start = 0
    rollingSum = 0
    currentIndex = 0

    while(currentIndex < targetIndex and start < targetIndex): 
        if rollingSum == target: 
            return (start, currentIndex - 1)
        elif rollingSum < target: 
            rollingSum += numbers[currentIndex]
            currentIndex += 1
        elif rollingSum > target: 
            rollingSum -= numbers[start]
            start += 1
    return (0, 0)

def q1(input): 
    badNumber, index = findBadNumber(input, 25)
    return badNumber

def q2(input): 
    targetNumber, targetNumberIndex  = findBadNumber(input, 25)
    start, end = findContiguousSum(input, targetNumber, targetNumberIndex)

    return min(input[start:end + 1]) + max(input[start:end + 1])



print(q1(input))
print(q2(input))
