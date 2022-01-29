import math

INFINITY = math.inf

def floydWarshall(adjacencyMatrix, numberOfVertices):
  dist = adjacencyMatrix
  for k in range(numberOfVertices):
    for i in range(numberOfVertices):
      for j in range(numberOfVertices): 
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
  return dist


matrix = [[0, 5, INFINITY, 10],
         [INFINITY, 0, 3, INFINITY],
         [INFINITY, INFINITY, 0,   1],
         [INFINITY, INFINITY, INFINITY, 0]
         ]

print(floydWarshall(matrix, 4))