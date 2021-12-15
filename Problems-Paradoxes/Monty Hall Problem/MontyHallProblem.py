import random


class Game:

    def __init__(self, changeDoor: bool = False):
        self.doors = ['Goat'] * 3
        self.doorWithCar = random.randint(0, 2)
        self.doors[self.doorWithCar] = 'Car'
        self.userChoice = random.randint(0, 2)
        self.firstGoatIndex, self.secondGoatIndex = self._chooseGoats()
        self.changeDoor = changeDoor

    def _chooseGoats(self):
        if self.doorWithCar == 0:
            return 1, 2
        elif self.doorWithCar == 1:
            return 0, 2
        elif self.doorWithCar == 2:
            return 0, 1

    def reveal(self, indexlist):
        index = random.choice(indexlist)
        doorsToReveal = ['X'] * 3
        doorsToReveal[index] = 'Goat'
        return index

    def play(self):
        if self.userChoice == self.firstGoatIndex:
            i = self.reveal([self.secondGoatIndex])
        elif self.userChoice == self.secondGoatIndex:
            i = self.reveal([self.firstGoatIndex])
        else:
            i = self.reveal([self.firstGoatIndex, self.secondGoatIndex])

        if self.changeDoor:
            # Choose the last door previously unchosen by either the player or the host
            self.userChoice = 3 - self.userChoice - i

    def getResult(self):
        return self.userChoice == self.doorWithCar

wins = 0

# If we don't change the door: average win rate is ~33%
# If we change the door: average win rate is ~66%

for i in range(1000):
    game = Game(True)
    game.play()
    if game.getResult():
        wins += 1

print(wins)
