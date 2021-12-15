numberOfNodes, keyNode = [int(i) for i in input().split()]

adjacencyMatrix = [[0] * numberOfNodes for _ in range(numberOfNodes)]

for y in range(numberOfNodes):
    temp = input().split()
    for x in range(numberOfNodes):
        adjacencyMatrix[y][x] = int(temp[x])

visitedNodes = [False] * numberOfNodes
visitedNodes[keyNode-1] = True


def countChildren(nodeFrom):
    counter = 1
    for i in range(numberOfNodes):
        if adjacencyMatrix[nodeFrom][i] == 1 and not visitedNodes[i]:
            visitedNodes[i] = True
            counter += countChildren(i)
    return counter


print(countChildren(keyNode-1))
