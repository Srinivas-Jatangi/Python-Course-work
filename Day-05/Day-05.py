a=10
b=20
a+b
30
a-b
-10
a*b
200
a/b
0.5
a//b
0
a%b
10
a**b
100000000000000000000
#comparision operators
a=20
b=10
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
#Assignment operators
c=30
c +=10
c
40
c -
SyntaxError: invalid syntax
c-=10
c
30
c *=2
c
60
c /=5
c
12.0
c //=5
c
2.0
c %=3
c
2.0
c**=2
c
4.0
#Logical operators
a=20
a%2==0
True
a%2==0 and a>10
True
b
10
b%2==0 and b>10
False
b%2==0 or b>10
True
b%2==0
True
not b%2==0
False
#and means all values true
#or means any one is true
#not means negetive
#MEMBER SHIP OPERATORS
s='python'
s
'python'
'p'in s
True
't'in s
True
'e'in s
False
'd'not in s
True
'p 'not in s
True
'p' not in s
False
>>> l=['java','python','c','flask']
>>> l
['java', 'python', 'c', 'flask']
>>> 'java' in l
True
>>> 'sql' in l
False
>>> 'c++' not in l
True
>>> 'java' not in l
False
>>> t=(1,2,3,4)
>>> 1 in t
True
>>> 7 in t
False
>>> 3 not in t
False
>>> 5 not in t
True
>>> s={1,2,3,4}
>>> 1 in s
True
>>> 6 in s
False
>>> 5 not in s
True
>>> d={1:2,3:4,5:6}
>>> 1 in d
True
>>> 2 in d
False
>>> 4  not in d
True
>>> 3 not in d
False
>>> #IDENTITY OPERATORS
>>> l=[1,2,3,4]
>>> m=[1,2,3,4]
>>> id(l)
4407249408
>>> id(m)
4327709632
>>> l==m
True
>>> id(l)==id(m)
False
>>> l is m
False
>>> n==m
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    n==m
NameError: name 'n' is not defined
>>> n=m
>>> n
[1, 2, 3, 4]
>>> n==m
True
>>> n is m
True
>>> id(n)
4327709632
>>> id(m)
4327709632
>>> n is not m
False
>>> n is not l
True
