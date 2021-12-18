import os


def checkIfInputTxtFileExists():
    if not os.path.isfile('input.txt'):
        createInputTxtFile()


def createInputTxtFile():
    with open('input.txt', 'w') as f:
        f.write('2 3 1 14 41 515 151351 1 3 43 4')
