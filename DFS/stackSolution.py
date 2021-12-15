numberOfNodes, keyNode = [int(i) for i in input().split()]

adjacencyMatrix = [[0] * numberOfNodes for _ in range(numberOfNodes)]

for y in range(numberOfNodes):
    temp = input().split()
    for x in range(numberOfNodes):
        adjacencyMatrix[y][x] = int(temp[x])

nodesStack = [keyNode - 1]
visitedNodes = [False] * numberOfNodes
counter = 0

while nodesStack:
    currentNode = nodesStack[-1]

    for node in range(numberOfNodes):
        if adjacencyMatrix[currentNode][node] == 1 and not visitedNodes[node]:
            visitedNodes[node] = True
            nodesStack.append(node)
            counter += 1
            break
    else:
        nodesStack.pop()

print(counter)
