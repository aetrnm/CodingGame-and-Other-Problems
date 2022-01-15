from Graph import Graph

numberOfNodes = int(input())
numberOfLinks = int(input())

adjacencyMatrix = [[0] * numberOfNodes for _ in range(numberOfNodes)]

for _ in range(numberOfLinks):
    n1, n2 = [int(i) for i in input().split()]
    adjacencyMatrix[n1][n2] = 1
    adjacencyMatrix[n2][n1] = 1

startNode, finishNode = [int(i) for i in input().split()]

graph = Graph(numberOfNodes, adjacencyMatrix)

print(graph.BFS(startNode, finishNode))
