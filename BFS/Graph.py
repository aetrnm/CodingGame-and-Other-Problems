import queue


class Graph:
    def __init__(self, numberOfNodes, adjacencyMatrix):
        self.numberOfNodes = numberOfNodes
        self.adjacencyMatrix = adjacencyMatrix

    def BFS(self, startNode, finishNode):
        if startNode == finishNode:
            return 0

        visitingQueue = queue.Queue()
        visitingQueue.put(startNode)
        visitedNodes = [False] * self.numberOfNodes
        visitedNodes[startNode] = True
        visitingSequence = [-1] * self.numberOfNodes
        wayExists = False

        while not visitingQueue.empty():
            currentNode = visitingQueue.get()

            for i in range(self.numberOfNodes):
                if self.adjacencyMatrix[currentNode][i] == 1 and not visitedNodes[i]:
                    visitingQueue.put(i)
                    visitedNodes[i] = True
                    visitingSequence[i] = currentNode

                    if i == finishNode:
                        wayExists = True
                        break

        return giveBFSPath(visitingSequence, finishNode)


def giveBFSPath(visitingSequence, finishNode):
    nextNode = finishNode
    ans = [nextNode]
    while True:
        nextNode = visitingSequence[nextNode]
        if nextNode == -1:
            ans.reverse()
            return ans
        ans.append(nextNode)
