# Найти кратчайший путь между двумя вершинами графа и запоминать путь
import sys
import queue

numberOfNodes = int(input())

adjacencyMatrix = [[0] * numberOfNodes for _ in range(numberOfNodes)]

for y in range(numberOfNodes):
    temp = input().split()
    for x in range(numberOfNodes):
        adjacencyMatrix[y][x] = int(temp[x])

startNode, finishNode = [int(i) - 1 for i in input().split()]

if startNode == finishNode:
    print(0)
    sys.exit()

visitingQueue = queue.Queue()
visitingQueue.put(startNode)
visitedNodes = [False] * numberOfNodes
visitedNodes[startNode] = True
visitingSequence = [-1] * numberOfNodes
wayExists = False

while not visitingQueue.empty():
    currentNode = visitingQueue.get()

    for i in range(numberOfNodes):
        if adjacencyMatrix[currentNode][i] == 1 and not visitedNodes[i]:
            visitingQueue.put(i)
            visitedNodes[i] = True
            visitingSequence[i] = currentNode

            if i == finishNode:
                wayExists = True
                break


def giveBFSPath():
    nextNode = finishNode
    ans = [nextNode+1]
    while True:
        nextNode = visitingSequence[nextNode]
        if nextNode == -1:
            ans.reverse()
            return ans
        ans.append(nextNode+1)


def printPathAndPathLength():
    BFSPath = giveBFSPath()
    print(len(BFSPath) - 1)
    print(' '.join(str(v) for v in BFSPath))


if not wayExists:
    print(-1)
else:
    printPathAndPathLength()
