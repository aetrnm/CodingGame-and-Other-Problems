numberOfNodes, numberOfLinks, numberOfExits = [int(i) for i in input().split()]

adjacencyMatrix = []
for i in range(numberOfNodes):
    adjacencyMatrix.append([0] * numberOfNodes)
# adjacencyMatrix = [[0]*numberOfNodes for _ in range(numberOfNodes)]

for i in range(numberOfLinks):
    node1, node2 = [int(j) for j in input().split()]
    adjacencyMatrix[node1][node2] = 1
    adjacencyMatrix[node2][node1] = 1

exits = []
for i in range(numberOfExits):
    exitNode = int(input())
    exits.append(exitNode)

# game loop
while True:
    virusNode = int(input())  # Index of node where virus is located


