import os


def createInputTxtFile():
    with open('input.txt', 'w') as f:
        f.write('2 3 1 14 41 515 151351 1 3 43 4')


if not os.path.isfile('input.txt'):
    createInputTxtFile()

with open('input.txt') as f:
    arr = f.readline()
    arr = [int(i) for i in arr.split()]


def mergeSort(array):
    arrayLength = len(array)

    if arrayLength == 1:
        return array

    middle = arrayLength // 2

    leftPart = mergeSort(array[:middle])
    rightPart = mergeSort(array[middle:])

    return merge(leftPart, rightPart)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


print(mergeSort(arr))
