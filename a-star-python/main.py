import sys

from Labyrinth import Labyrinth
import heapq

with open('./field2.txt') as f:
    contents = f.readlines()

labyrinth = Labyrinth(contents)

priorityQueue = [(labyrinth.getHeuristicPriority(labyrinth.start, -1), labyrinth.start)]

while priorityQueue:
    labyrinth.printLabyrinth()
    priority, currentCell = heapq.heappop(priorityQueue)
    currentCell.inQueue, currentCell.visited = False, True
    neighbours: list = labyrinth.getWalkableNeighbours(currentCell)
    for cell in neighbours:
        heapq.heappush(priorityQueue, (labyrinth.getHeuristicPriority(cell, currentCell.distanceFromStart), cell))
        cell.inQueue = True
        cell.distanceFromStart = currentCell.distanceFromStart + 1

        if cell.isFinish:
            print(labyrinth.finish.distanceFromStart)
            sys.exit()
