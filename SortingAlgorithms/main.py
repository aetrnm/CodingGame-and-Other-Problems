from SortingAlgorithms import SortingAlgorithms
from Helper import checkIfInputTxtFileExists

checkIfInputTxtFileExists()

with open('input.txt') as f:
    arr = f.readline()
    arr = [int(i) for i in arr.split()]

SA = SortingAlgorithms()

print(SA.heapSort(arr))
