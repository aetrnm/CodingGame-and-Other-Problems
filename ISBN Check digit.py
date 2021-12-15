import re

invalidList = []


def checkValidity(num):
    if len(num) != 10 and len(num) != 13:
        return False

# 234564321345543245 <- no match
# 213455432X <- match
# ^ <- string start
# \d === [0-9]
# {9} <- previous symbol exactly 9 times
# \d{9} <- exactly 9 digits
# ( [a-z]{5} <- a word of exactly five letters )
# () <- a group of elements
# | <- OR
# \d|X <- a digit or an X
# $ <- string end
# ( [A-Z]{2}\d{4}[A-Z]{2} <- auto numbers )
    s = 0
    if len(num) == 10:
        if not re.fullmatch(r"^\d{9}(\d|X)$", num):
            return False

        for i in range(9):
            s += int(num[i]) * (10 - i)

        realCheckDigit = (11 - s) % 11
        if num[9] == 'X':
            return realCheckDigit == 10
        return realCheckDigit == int(num[9])

    if len(num) == 13:
        if not re.fullmatch(r"^\d{12}(\d|X)$", num):
            return False

        for i in range(12):
            if i % 2 == 0:
                s += int(num[i]) * 1
            else:
                s += int(num[i]) * 3

        realCheckDigit = (10 - s) % 10
        if num[12] == 'X':
            return False
        return realCheckDigit == int(num[12])


n = int(input())
for i in range(n):
    isbn = input()

    if not checkValidity(isbn):
        invalidList.append(isbn)

print(str(len(invalidList)) + " invalid:")
for num in invalidList:
    print(num)
