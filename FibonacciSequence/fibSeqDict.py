fibonacciSequence = {}

def getFibSeqNumber(n):
  if n in fibonacciSequence:
    return fibonacciSequence[n]

  if n == 1 or n == 0:
    return n

  nthNumber = (getFibSeqNumber(n-1) + getFibSeqNumber(n-2))%100
  fibonacciSequence[n] = nthNumber
  return nthNumber

n = int(input())
print(getFibSeqNumber(n))