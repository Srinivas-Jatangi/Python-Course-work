Python 3.15.1 (tags/v3.15.1:c37e74c, Oct 21 2026, 06:24:08) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
a
10
10
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
bool(a)
True
int(a)
10
10
10
b = 'codegyan'
float(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(b)
ValueError: could not convert string to float: 'codegyan'
int(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: 'codegyan'
set(b)
{'g', 'y', 'n', 'c', 'e', 'o', 'd', 'a'}
bool(b)
True
bool(0.0)
False
dict(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
int(b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: 'codegyan'
complex(b)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    complex(b)
ValueError: complex() arg is a malformed string
complex(a)
(10+0j)
string(a)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    string(a)
NameError: name 'string' is not defined. Did you forget to import 'string'?
string(b)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    string(b)
NameError: name 'string' is not defined. Did you forget to import 'string'?
list(a)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
list(b)
['c', 'o', 'd', 'e', 'g', 'y', 'a', 'n']
c = 3+4j
string(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    string(c)
NameError: name 'string' is not defined. Did you forget to import 'string'?
complex(c)
(3+4j)
int(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
lidt(c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    lidt(c)
NameError: name 'lidt' is not defined. Did you mean: 'list'?
list(c)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
list(c)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
float(c)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
float(a)
10.0
a = '1019'
int(a)
1019
float(a)
1019.0
bool(a)
True
t=(1,2,3,4)
int(t)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
tuple(t)
(1, 2, 3, 4)
set(t)
{1, 2, 3, 4}
int(a)
1019
complex(t)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not tuple
complax(a)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    complax(a)
NameError: name 'complax' is not defined. Did you mean: 'complex'?
complex(a)
(1019+0j)
str(a)
'1019'
list(a)
['1', '0', '1', '9']
>>> list(t)
[1, 2, 3, 4]
>>> list(c)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
>>> list(b)
['c', 'o', 'd', 'e', 'g', 'y', 'a', 'n']
>>> bool(a)
True
>>> a = 3440
>>> a
3440
>>> float(a)
3440.0
>>> int(a)
3440
>>> str(a)
'3440'
>>> bool(a)
True
>>> complex(a)
(3440+0j)
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> ....
SyntaxError: invalid syntax
>>> int -> float,complex,s,b
SyntaxError: invalid syntax
>>> int - > float,complex,s,b
SyntaxError: invalid syntax
>>> '''
... int  -> float,complex,s,b
... fl->in,com,s,b
... com->s,b
