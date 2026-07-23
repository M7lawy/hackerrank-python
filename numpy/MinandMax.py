import numpy



n,m = map(int, input().split())

myList = []

for _ in range(n):

    row = list(map(int, input().split()))

    myList.append(row)

newList = numpy.array(myList)

minList = numpy.min(newList, axis=1)

print(numpy.max(minList))
