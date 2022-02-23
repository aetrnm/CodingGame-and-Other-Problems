class Cell:

    def __init__(self, x=0, y=0, isStart=False, isFinish=False, isWall=False) -> None:
        self.isStart = isStart
        self.isFinish = isFinish
        self.isWall = isWall
        self.distanceFromStart = -1
        self.x = x
        self.y = y
        self.inQueue = False
        self.visited = False

    def __lt__(self, other):
        return 1
