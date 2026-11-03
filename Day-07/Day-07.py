Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s ='python programming'
s
'python programming'
s.startswith('p')
True
s.startswith("P")
False
s.startswith("pyt")
True
s.startswith("img")
False
s.startswith("ing")
False
s.endswith("img")
False
s.endswith("ing")
True
's'.islower()
True
'u'.isupper()
False
'codegnan@'.isalpha()
False
'code12'.isaplha()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    'code12'.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean '.isalpha' instead of '.isaplha'?
'code12'.isalpha()
False
'code'.isalpha()
True
'code123'.isalnum()
True
'code@123'.isalnum()
False
'code'.isalnum()
True
s
'python programming'
s.istitle()
False
'myvar'.isidentifier()
True
'my@var'.isidentifier()
False
''.isspace()
False
'        hello'.isspace()
False
'1234'.isdecimal()
True
'1234'.isdigit()
True
'1234'.isnumeric()
True
'a b c d'.split()
['a', 'b', 'c', 'd']
'a,b,c,d'.split()
['a,b,c,d']
'a,b,c,d'.split(',')
['a', 'b', 'c', 'd']
'a-b-c-d'.split('-')
['a', 'b', 'c', 'd']
'a-b-c-d'.split('-',2)
['a', 'b', 'c-d']
'a-b-c-d'.rsplit('-')
['a', 'b', 'c', 'd']
'a-b-c-d'.rsplit('-',2)
['a-b', 'c', 'd']
s="""
hello
world
python
"""
s
'\nhello\nworld\npython\n'
s.splitlines()
['', 'hello', 'world', 'python']
1=['a', 'b', 'c', 'd']
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1 =['a', 'b', 'c', 'd']
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1=['a', 'b', 'c', 'd']
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1=['a', 'b', 'c', 'd']
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=['a', 'b', 'c', 'd']
'-'.join(l)
'a-b-c-d'
'@'.join(l)
'a@b@c@d'
'*'.join(l)
'a*b*c*d'
''.join(l)
'abcd'
s
'\nhello\nworld\npython\n'
s='a-b-c-d'
s.partition('b')
('a-', 'b', '-c-d')
'python.py'.partition('.')
('python', '.', 'py')
'pyt.hon.py'.partition('.')
('pyt', '.', 'hon.py')
'pyt.hon.py'.rpartition('.')
('pyt.hon', '.', 'py')
s="hello"
s.encode()
b'hello'
t = "hello ㋡ "
t.encode()
b'hello \xe3\x8b\xa1 '
b'hello \xe3\x8b\xa1 '.decode()
'hello ㋡ '
l=[]
l=list()
l=[1,2,3]
l=list([1,2,3,4])
l
[1, 2, 3, 4]
type (l)
<class 'list'>
#mut ord dup het dyn
l=[2,3,4,5,5]
l
[2, 3, 4, 5, 5]
l=[1,1,1,1,1,1]
l
[1, 1, 1, 1, 1, 1]
l=[1,12.2,3+5j,"str",[1,2],(1,2),{1,2},{1:2},False,None]
l
[1, 12.2, (3+5j), 'str', [1, 2], (1, 2), {1, 2}, {1: 2}, False, None]
[1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
[1,2,3]*5
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
l =['python','java','c','flask','fastapi','mysql','aws']
l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
l[0]
'python'
l[-1]
'aws'
l[-2]
'mysql'
l[2]
'c'
l[3]
'flask'
l[4]
'fastapi'
l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
l[:3]
['python', 'java', 'c']
l[-3:]
['fastapi', 'mysql', 'aws']
l[2:5]
['c', 'flask', 'fastapi']
l[1:2]
['java']
l[1::2]
['java', 'flask', 'mysql']
l[::2]
['python', 'c', 'fastapi', 'aws']
l[::-1]
['aws', 'mysql', 'fastapi', 'flask', 'c', 'java', 'python']
l[-3:-6:-1]
['fastapi', 'flask', 'c']
l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
'c'in l
True
'mysql' in l
True
'html' not in l
True
'css' in l
False
l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
len(l)
7
sorted(l)
['aws', 'c', 'fastapi', 'flask', 'java', 'mysql', 'python']
>>> max(l)
'python'
>>> min(l)
'aws'
>>> l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
>>> id(1)
140719675630864
>>> l[l]
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    l[l]
TypeError: list indices must be integers or slices, not list
>>> l[1]
'java'
>>> l[1]='html'
>>> l
['python', 'html', 'c', 'flask', 'fastapi', 'mysql', 'aws']
>>> id(l)
1959308429824
>>> l[2]='c++'
>>> l
['python', 'html', 'c++', 'flask', 'fastapi', 'mysql', 'aws']
>>> l[3]='css'
>>> l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql', 'aws']
>>> id(l)
1959308429824
>>> l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql', 'aws']
>>> l.append('a')
>>> l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql', 'aws', 'a']
>>> l.append('b')
>>> l.append
<built-in method append of list object at 0x000001C82FE20A00>
>>> l.append('c')
>>> l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql', 'aws', 'a', 'b', 'c']
>>> id(l)
1959308429824
>>> l.extend([1,2,3,4,4])
>>> l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql', 'aws', 'a', 'b', 'c', 1, 2, 3, 4, 4]
>>> l.insert(1,'flask')
>>> l
['python', 'flask', 'html', 'c++', 'css', 'fastapi', 'mysql', 'aws', 'a', 'b', 'c', 1, 2, 3, 4, 4]
>>> l.insert(2,'c')
>>> l
['python', 'flask', 'c', 'html', 'c++', 'css', 'fastapi', 'mysql', 'aws', 'a', 'b', 'c', 1, 2, 3, 4, 4]
>>> id(l)
1959308429824
