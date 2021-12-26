import math


class SortingAlgorithms:

    def mergeSort(self, array: list) -> list:
        arrayLength = len(array)

        if arrayLength == 1:
            return array

        middle = arrayLength // 2

        leftPart = self.mergeSort(array[:middle])
        rightPart = self.mergeSort(array[middle:])

        return mergeArrays(leftPart, rightPart)

    def countingSort(self, array: list, minValue: int, maxValue: int) -> list:
        values = [0] * (maxValue - minValue + 1)

        for value in array:
            values[value - minValue] += 1

        ans = [0] * len(array)
        curValue = minValue
        k = 0
        for numberOfRepeats in values:
            for _ in range(numberOfRepeats):
                ans[k] = curValue
                k += 1
            curValue += 1
        return ans

    def monkeySort(self, array: list) -> list:
        from random import shuffle
        while not isSorted(array):
            shuffle(array)
        return array

    def quickSort(self, array: list) -> list:
        if len(array) < 2:
            return array
        barrierIndex = math.ceil(len(array) / 2)
        barrierElement = array[barrierIndex]
        array[barrierIndex], array[0] = array[0], array[barrierIndex]
        leftIt = 1
        rightIt = len(array) - 1
        while True:
            while leftIt <= rightIt and array[leftIt] < barrierElement:
                leftIt += 1
            while rightIt > leftIt and array[rightIt] > barrierElement:
                rightIt -= 1
            if leftIt >= rightIt:
                break
            array[leftIt], array[rightIt] = array[rightIt], array[leftIt]

        array[0], array[leftIt - 1] = array[leftIt - 1], array[0]

        return self.quickSort(array[:leftIt - 1]) + [barrierElement] + self.quickSort(array[leftIt:])

    def heapSort(self, array: list) -> list:
        createMaxHeap(0, array)
        for currentSubArraySize in range(len(array)-1, -1, -1):
            array[0], array[currentSubArraySize] = array[currentSubArraySize], array[0]
            siftDown(0, array, currentSubArraySize)
        return array


def siftDown(i: int, array: list, currentSubArraySize):
    leftI = i * 2 + 1
    rightI = i * 2 + 2

    leftChild = array[leftI] if leftI < currentSubArraySize else -math.inf
    rightChild = array[rightI] if rightI < currentSubArraySize else -math.inf
    elements = [array[i], leftChild, rightChild]
    tempMax = max(elements)

    if tempMax == rightChild:
        array[i], array[rightI] = array[rightI], array[i]
        siftDown(rightI, array, currentSubArraySize)
    elif tempMax == leftChild:
        array[i], array[leftI] = array[leftI], array[i]
        siftDown(leftI, array, currentSubArraySize)


def createMaxHeap(i: int, array: list) -> None:
    arraySize = len(array)
    leftI = i * 2 + 1
    rightI = i * 2 + 2
    if leftI < arraySize:
        createMaxHeap(leftI, array)
    if rightI < arraySize:
        createMaxHeap(rightI, array)
    siftDown(i, array, arraySize)


def mergeArrays(left: list, right: list) -> list:
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


def isSorted(arr: list) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
