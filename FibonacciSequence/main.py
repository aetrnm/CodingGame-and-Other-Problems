from fibonacciVariations import *

for i in range(1, 1_000_000_000, 1_000_000):
    print(f'Naive {i}th {fibNaive(i)}')
    print(f'Long {i}th {fibLong(i)}')
    print(f'Advanced {i}th {fibAdvanced(i)}')
    print()
