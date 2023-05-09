import sys
# print(sys.builtin_module_names)
import pandas
import numpy
numpy.array([1,2,3,4,5])
#얘랑 비슷해 보이지만 다름 lst=[1,2,3,4,5]
print(type(numpy.array([1,2,3,4,5])))

arrA=numpy.array([1,2,3,4,5])
arrB=numpy.array([6,7,8,9,10])

print(arrA+arrB)
print(arrA-arrB)
print(arrA*arrB)
print(arrA/arrB)
print(arrA%arrB)

import math

print(math.fsum([1,2,3]))
from math import gcd
print(math.gcd(10,20))

print(math.ceil(5.333))
import hello as h
h.helloworld()

from hong.dataanalysis import hellodata
hellodata.helloworld()