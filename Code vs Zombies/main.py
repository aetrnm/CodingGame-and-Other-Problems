import sys
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
import math


def calculateDistance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def calculateZombieStepsToReachTarget(x1, y1, x2, y2):
    zombieSpeed = 400
    return math.ceil(calculateDistance(x1, y1, x2, y2) / zombieSpeed)


def calculateAshStepsToReachTarget(x1, y1, x2, y2):
    AshSpeed = 1000
    return math.ceil(calculateDistance(x1, y1, x2, y2) / AshSpeed)


def calculateAshStepsToKillTarget(x1, y1, x2, y2):
    AshSpeed = 1000
    return math.ceil(calculateDistance(x1, y1, x2, y2) / AshSpeed)


while True:
    humans = {}
    zombies = {}
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans[human_id] = (human_x, human_y)
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_x_next, zombie_y_next = [int(j) for j in input().split()]
        zombies[zombie_id] = (zombie_x, zombie_y)

    currentMinimumDistance = math.inf
    zombieIdToGo = -1

    for humanId in humans:
        humanX, humanY = humans[humanId]
        for zombieId in zombies:
            zombieX, zombieY = zombies[zombieId]
            distanceToCurrentHuman = calculateDistance(humanX, humanY, zombieX, zombieY)
            if distanceToCurrentHuman < currentMinimumDistance:
                currentMinimumDistance = distanceToCurrentHuman
                zombieIdToGo = zombieId

    print(f"{zombies[zombieIdToGo][0]} {zombies[zombieIdToGo][1]}")
