class Cell:
  def __init__(self, isStart=False, isFinish=False, isWall=False) -> None:
    self.isStart = isStart
    self.isFinish = isFinish
    self.isWall = isWall
    self.GDistance = -1 # distance from start to node
    self.HDistance = -1 # distance from node to finish
    self.FDistance = 0 # GDistance + HDistance
    self.x = 0
    self.y = 0
    self.parent = None