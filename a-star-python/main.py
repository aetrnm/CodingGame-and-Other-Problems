from multiprocessing.dummy import current_process
from queue import Empty
from Cell import Cell


with open('./field.txt') as f:
    contents = f.readlines()


height = len(contents)
width = len(contents[0])-1
matrix = [[Cell() for x in range(width)] for y in range(height)]

startX = -1
startY = -1
finishX = -1
finishY = -1

for y in range(height):
  for x in range(width):
    matrix[y][x].x = x
    matrix[y][x].y = y
    if contents[y][x] == 'S':
      matrix[y][x].isStart = True
      matrix[y][x].GDistance = 0
      startX = x
      startY = y
    if contents[y][x] == 'F': 
      matrix[y][x].isFinish = True
      matrix[y][x].HDistance = 0
      finishX = x
      finishY = y
    if contents[y][x] == '#': 
      matrix[y][x].isWall = True


def getHeuristicDistanceToFinish(cell: Cell):
  return abs(finishX - cell.x) + abs(finishY - cell.y)

def getDistanceFromStartTo(cell: Cell):
  return abs(startX - cell.x) + abs(startY - cell.y)

# Filling H and G distances
for y in range(height):
  for x in range(width):
    if not matrix[y][x].isWall:
      matrix[y][x].HDistance = getHeuristicDistanceToFinish(matrix[y][x])
      matrix[y][x].GDistance = getDistanceFromStartTo(matrix[y][x])
      matrix[y][x].FDistance = matrix[y][x].HDistance + matrix[y][x].GDistance

def printHDistances():
  print('HDISTANCES: ')
  for y in range(height):
    for x in range(width):
      print(f'{matrix[y][x].HDistance:02}', end=' ')
    print()

def printGDistances():
  print('GDISTANCES: ')
  for y in range(height):
    for x in range(width):
      print(f'{matrix[y][x].GDistance:02}', end=' ')
    print()


frontier = [matrix[startY][startX]]
closedList = []

def inBounds(y, x):
  iHeight = height-1
  iWidth = width-1
  return y >= 0 and y <= iHeight and x >= 0 and x <= iWidth


def getWalkableNeighbours(cell):
  ans = []
  if inBounds(cell.y-1, cell.x-1) and not matrix[cell.y-1][cell.x-1].isWall:
    lt = matrix[cell.y-1][cell.x-1]
    if lt not in closedList:
      ans.append(lt)
  if inBounds(cell.y-1, cell.x) and not matrix[cell.y-1][cell.x].isWall:
    t = matrix[cell.y-1][cell.x]
    if t not in closedList:
      ans.append(t)
  if inBounds(cell.y-1, cell.x+1) and not matrix[cell.y-1][cell.x+1].isWall:
    rt = matrix[cell.y-1][cell.x+1]
    if rt not in closedList:
      ans.append(rt)

  if inBounds(cell.y, cell.x-1) and not matrix[cell.y][cell.x-1].isWall:
    l = matrix[cell.y][cell.x-1]
    if l not in closedList:
      ans.append(l)
  if inBounds(cell.y, cell.x+1) and not matrix[cell.y][cell.x+1].isWall:
    r = matrix[cell.y][cell.x+1]
    if r not in closedList:
      ans.append(r)

  if inBounds(cell.y+1, cell.x-1) and not matrix[cell.y+1][cell.x-1].isWall:
    lb = matrix[cell.y+1][cell.x-1]
    if lb not in closedList:
      ans.append(lb)
  if inBounds(cell.y+1, cell.x) and not matrix[cell.y+1][cell.x].isWall:
    b = matrix[cell.y+1][cell.x]
    if b not in closedList:
      ans.append(b)
  if inBounds(cell.y+1, cell.x+1) and not matrix[cell.y+1][cell.x+1].isWall:
    rb = matrix[cell.y+1][cell.x+1]
    if rb not in closedList:
      ans.append(rb)

  return ans

while frontier:
  currentCell = frontier[0]
  neighbours = getWalkableNeighbours(currentCell)
  for cell in neighbours:
    if not cell in frontier:
      cell.parent = currentCell
      frontier.append(cell)
      
  break