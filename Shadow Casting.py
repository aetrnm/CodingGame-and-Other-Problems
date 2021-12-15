n = int(input())
initialImage = []
for y in range(n):
    line = list(input())
    initialImage.append(line)
longest = max([len(line) for line in initialImage])
for i in range(2):
    initialImage.append([' '] * (longest + 2))
for line in initialImage:
    curLen = len(line)
    needToAdd = longest - curLen + 2
    line += [' '] * needToAdd

shadows = [initialImage[0]]
for y in range(1, n+2):
    shadows.append([' '] * (longest + 2))
    shadows[y][0] = initialImage[y][0]
    for x in range(1, longest + 2):
        if initialImage[y][x] != ' ':
            shadows[y][x] = initialImage[y][x]
        elif initialImage[y-1][x-1] != ' ':
            shadows[y][x] = '-'
        elif x > 1 and y > 1 and initialImage[y-2][x-2] != ' ':
            shadows[y][x] = '`'

for line in shadows:
    print(''.join(line).rstrip())
