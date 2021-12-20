class SortingAlgorithms:

    def mergeSort(self, array) -> list:
        arrayLength = len(array)

        if arrayLength == 1:
            return array

        middle = arrayLength // 2

        leftPart = self.mergeSort(array[:middle])
        rightPart = self.mergeSort(array[middle:])

        return mergeArrays(leftPart, rightPart)

    def countingSort(self, array, minValue, maxValue) -> list:
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

    def monkeySort(self, array):
        from random import shuffle
        while not isSorted(array):
            shuffle(array)
        return array

    # TODO: quick sort
    def quickSort(self, array):
        if len(array) < 2:
            return array
        barrierIndex = len(array) // 2
        barrierElement = array[barrierIndex]
        leftIt = 0
        rightIt = len(array) - 1
        while leftIt < rightIt:
            while array[leftIt] < barrierElement and leftIt <= len(array) - 1:
                leftIt += 1
            while array[rightIt] >= barrierElement and rightIt >= 0:
                rightIt -= 1

            array[leftIt], array[rightIt] = array[rightIt], array[leftIt]
            leftIt += 1
            rightIt -= 1

        print('Array after while cycle: ', array)
        print('Left part: ', array[:barrierIndex])
        print('Barrier element is: ', barrierElement)
        print('Right part: ', array[barrierIndex + 1:])
        print()

        return self.quickSort(array[:barrierIndex]) + [barrierElement] + self.quickSort(array[barrierIndex + 1:])


def mergeArrays(left, right):
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
