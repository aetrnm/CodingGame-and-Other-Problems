import queue, math

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

nodesNumber, linksNumber, exitsNumber = [int(i) for i in input().split()]
adjacencyMatrix = [[0] * nodesNumber for _ in range(nodesNumber)]

for i in range(linksNumber):
  n1, n2 = [int(j) for j in input().split()]
  adjacencyMatrix[n1][n2] = 1
  adjacencyMatrix[n2][n1] = 1

myGraph = Graph(nodesNumber, adjacencyMatrix)

blueNodes = []
for i in range(exitsNumber):
  blueNode = int(input())
  blueNodes.append(blueNode)

while True:
  virusNode = int(input())

  minimumLengthBetweenVirusAndBlueNode = math.inf
  minimunPathBetweenVirusAndBlueNode = []
  for startNode in blueNodes:
    finishNode = virusNode
    currentPath = myGraph.BFS(startNode, finishNode)
    if len(currentPath) < minimumLengthBetweenVirusAndBlueNode:
      minimumLengthBetweenVirusAndBlueNode = len(currentPath)
      minimunPathBetweenVirusAndBlueNode = currentPath

  print(f"{minimunPathBetweenVirusAndBlueNode[0]} {minimunPathBetweenVirusAndBlueNode[1]}")