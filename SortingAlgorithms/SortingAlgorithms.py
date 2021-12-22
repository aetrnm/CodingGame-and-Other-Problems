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

    # TODO: quick sort

    def quickSort(self, array: list) -> list:
        if len(array) < 2:
            return array
        barrierIndex = math.ceil(len(array) / 2)
        barrierElement = array[barrierIndex]
        print('Initial array:', array)
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
            print('Array of each iteration: ', array)
            array[leftIt], array[rightIt] = array[rightIt], array[leftIt]

        array[0], array[leftIt-1] = array[leftIt-1], array[0]
        print('Array before division', array)

        print('Left iterator: ', leftIt)
        print('Right iterator: ', rightIt)
        print('Left part: ', array[:leftIt-1])
        print('Barrier element is: ', barrierElement)
        print('Right part: ', array[leftIt:])
        print()

        return self.quickSort(array[:leftIt-1]) + [barrierElement] + self.quickSort(array[leftIt:])


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
