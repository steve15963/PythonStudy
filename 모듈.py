import math
import module.fibo as fibo
from module.fibo import fibo as f1, fibo2 as f2
import imp
import sys
print(math.pi)

fibo.fibo(5)

data = fibo.fibo2(5)

print(data)

f1(5)

data = f2(20)
print(data)

imp.reload(math)

print(math.pi)


#print(dir(sys))
print(dir(f1))

print(sys.path)