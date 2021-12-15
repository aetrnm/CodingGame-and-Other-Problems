import random


def isLeapYear(year: int):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


class Game:

    def __init__(self, numberOfPeople):
        self.numberOfPeople: int = numberOfPeople
        self.listOfPeople = []

        for i in range(self.numberOfPeople):
            year = random.randint(1900, 2020)
            day = -1
            if isLeapYear(year):
                day = random.randint(1, 366)
            elif not isLeapYear(year):
                day = random.randint(1, 365)

            self.listOfPeople.append(day)

        self.listOfLeftDates = set(self.listOfPeople)

    def getResult(self):
        if self.numberOfPeople != len(self.listOfLeftDates):
            return True
        elif self.numberOfPeople == len(self.listOfLeftDates):
            return False


# for 10 people: less than 15%
# for 100 people: 99.9%
# for 23 people: ~50%

wins = 0
for i in range(100):
    game = Game(23)
    if game.getResult():
        wins += 1

print(wins)
