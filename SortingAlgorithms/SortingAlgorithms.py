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


class SortingAlgorithms:

    def mergeSort(self, array):
        arrayLength = len(array)

        if arrayLength == 1:
            return array

        middle = arrayLength // 2

        leftPart = self.mergeSort(array[:middle])
        rightPart = self.mergeSort(array[middle:])

        return mergeArrays(leftPart, rightPart)
