import numpy


theList = []


n , m = map(int, input().split())

for _ in range(n):

    row = list(map(int, input().split()))

    theList.append(row)

numpyArray = numpy.array(theList)

summ = numpy.sum(numpyArray, axis=0)

print(numpy.prod(summ))
    