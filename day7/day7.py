f = open("input.txt", "r")
input = []

for x in f: 
    input.append(x.strip())

f.close()


def buildTree(input): 
    nodes = {}
    for i in input: 
        iSplit = i.split(" ")
        rootColor = iSplit[0] +  " " + iSplit[1]
        nodes[rootColor] = set()

    for i in input: 
        i = i.replace(",", "")
        i = i.replace(".", "")
        iSplit = i.split(" ")

        rootColor = iSplit[0] + " " + iSplit[1]

        for j in range(3, len(iSplit)): 
            if iSplit[j] == "bag" or iSplit[j] == "bags": 
                if iSplit[j - 2] != "no": 

                    childColor = iSplit[j - 2] + " " + iSplit[j - 1]
                    nodes[childColor].add(rootColor)

    return nodes


def buildTreeWithQuantity(input): 
    nodes = {}
    for i in input: 
        iSplit = i.split(" ")
        rootColor = iSplit[0] +  " " + iSplit[1]
        nodes[rootColor] = set()

    for i in input: 
        i = i.replace(",", "")
        i = i.replace(".", "")
        iSplit = i.split(" ")

        rootColor = iSplit[0] + " " + iSplit[1]

        for j in range(3, len(iSplit)): 
            if iSplit[j] == "bag" or iSplit[j] == "bags": 
                if iSplit[j - 2] != "no": 
                    childColor = iSplit[j - 2] + " " + iSplit[j - 1]
                    quantity = int(iSplit[j - 3])
                    nodes[rootColor].add((childColor, quantity))

    return nodes


def q1(input, targetColor): 
    nodes = buildTree(input)

    s = []

    counter = set()
    s.append(targetColor)

    while(len(s) > 0): 
        current = s.pop()
        parents = nodes[current]
        for parent in parents: 
            counter.add(parent)
            s.append(parent)

    return(len(counter))

def q2(input, targetColor): 
    nodes = buildTreeWithQuantity(input)

    counter = 0
    s = []
    s.append(targetColor)

    while(len(s) > 0): 
        current = s.pop()
        parents = nodes[current]
        for parent in parents: 
            color, quantity = parent[0], parent[1]
            for i in range(0, quantity): 
                counter += 1
                s.append(color)

    return counter

print(q1(input, "shiny gold"))
print(q2(input, "shiny gold"))
