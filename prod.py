import numpy
list=[1,2,3,4]
n=len(list)
if n <3:
    print(" ")
list.sort(reverse=True)
print(list)
result=numpy.prod(list[:3])
print(result)
