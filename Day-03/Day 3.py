Python 3.15.1 (tags/v3.15.1:c37e74c, Oct 21 2026, 06:24:08) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
type(a)
<class 'int'>
b = 12.3
type(b)
<class 'float'>
c = 2+5j
c
(2+5j)
type(c)
<class 'complex'>
s = "Codegnan"
type(s)
<class 'str'>
s
'Codegnan'
1=[1,2,3,4,]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1=[1,2,3,4]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=[1,2,3,4]
type(l)
<class 'list'>
k=[1.23.4,
   
SyntaxError: invalid syntax. Perhaps you forgot a comma?
k=[1,23.4,"56",[1,2,3]]
k
[1, 23.4, '56', [1, 2, 3]]
type(k)
<class 'list'>
l=[1,1,1,1,1]
l
[1, 1, 1, 1, 1]
s='code'
id(s)
140720213918512
s+="gnan"
s
'codegnan'
id(s)
2882166589232
l=[1,2,3]
id(l)
2882204937664
l.append(12)
l.pop()
12
l
[1, 2, 3]
id(l)
2882204937664
l
[1, 2, 3]
t=(1,2,3,4)
>>> t=(1,1,1,1)
>>> t
(1, 1, 1, 1)
>>> t=(1,2.3)
>>> t
(1, 2.3)
>>> type(t)
<class 'tuple'>
>>> s={34,1234,124321,1325,34,34,34,34}
>>> s
{124321, 34, 1325, 1234}
>>> type(s)
<class 'set'>
>>> d={l:"one",2:4,3[1,2,3],5:(1,23)}
SyntaxError: ':' expected after dictionary key
>>> d={l:"one",2:4,3:[1,2,3],5:(1,23)}
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    d={l:"one",2:4,3:[1,2,3],5:(1,23)}
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
>>> d={1:"one",2:4,3:[1,2,3],5:(1,23)}
>>> d
{1: 'one', 2: 4, 3: [1, 2, 3], 5: (1, 23)}
>>> pro = {"pro_name":'laptop',"price":55000,discount':10}
...        
SyntaxError: unterminated string literal (detected at line 1)
>>> pro = {"pro_name":'laptop',"price":55000,"discount":10}
>>> pro
{'pro_name': 'laptop', 'price': 55000, 'discount': 10}
>>> type(d)
<class 'dict'>
>>> status =True
>>> type(status)
<class 'bool'>
>>> s = False
>>> type(s)
<class 'bool'>
>>> s=None
>>> type(s)
<class 'NoneType'>
