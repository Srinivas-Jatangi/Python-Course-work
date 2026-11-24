'''
import sys

print(sys.argv)
print(sys.path)
print(sys.version)
sys.exit()
print("Hello World")
'''
'''
import platform

print(platform.system(), platform.release(), platform.processor(),sep='\n')
'''
'''
import math

print(math.pi)
print(math.e)

print(math.sqrt(16))
print(math.sqrt(25))

print(math.pow(2,5))
print(math.pow(3,3))

print(round(12.0000001))
print(round(12.3))
print(round(12.8))
print(round(12.99999999))

print(math.ceil(12.0000001))
print(math.ceil(12.3))
print(math.ceil(12.8))
print(math.ceil(12.99999999))

print(math.floor(12.0000001))
print(math.floor(12.3))
print(math.floor(12.8))
print(math.floor(12.99999999))

print(abs(-120))
print(math.fabs(-120))

print(math.factorial(6))
print(math.gcd(12,16))

print(math.log(2,2))
print(math.sin(30))
print(math.cos(20))
print(math.tan(40))
print(math.degrees(120))
print(math.radians(120))
'''
'''
import random

random.seed(10)
print(random.random())
print(random.randint(1,10))
print(random.uniform(1,10))

l=['python','java','c','c++','flask','mysql','fastapi']

print(random.choice(l))
print(random.choices(l,k=3))

print(l)
random.shuffle(l)
print(l)
'''
'''
from collections import Counter

s = 'python programming'

print(Counter(s))

d = {}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)
'''
'''
from collections import Counter,defaultdict

s = 'python programming'

d = defaultdict(float)
for i in s:
    d[i]+=1
print(d)
'''
'''
from collections import Counter,defaultdict,deque

'''
'''
----------------------------
40
----------------------------
'''
'''

s = deque([])

s.append(10)
s.append(20)
s.append(30)
s.append(40)
s.popleft()
s.popleft()
s.popleft()

print(s)
'''
'''
from collections import Counter,defaultdict,deque

'''
'''
----------------------------
40 30
----------------------------
'''
'''

s = deque([])

s.appendleft(10)
s.appendleft(20)
s.appendleft(30)
s.appendleft(40)
s.pop()
s.pop()

print(s)
'''

from itertools import combinations,permutations

#abc - ab bc ac
#abc - ab ba bc cb ac ca

s='abcd'

print([''.join(i) for i in combinations(s,3)])
print([''.join(i) for i in permutations(s,3)])