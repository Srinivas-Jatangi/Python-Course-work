Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s ='python'
s
'python'
p=''
p
''
s
'python'
t='programming'
t
'programming'
s+t
'pythonprogramming'
t*3
'programmingprogrammingprogramming'
s*7
'pythonpythonpythonpythonpythonpythonpython'
'*'*20
'********************'
'0'*30
'000000000000000000000000000000'
s ='python java flask mysql fastapi'
s
'python java flask mysql fastapi'
s[0]
'p'
s[7]
'j'
s[-1]
'i'
s[-4]
't'
s[-7]
'f'
s[12]
'f'
s[6]
' '
s[4]
'o'
s[-18]
'l'
s
'python java flask mysql fastapi'
s[0:6:1]
'python'
s[7:11:1]
'java'
s
'python java flask mysql fastapi'
s[:6]
'python'
s[7:11]
'java'
s[18:23]
'mysql'
s[24]
'f'
s[24:]
'fastapi'
s[:-1]
'python java flask mysql fastap'
s[-7:]
'fastapi'
s[::2]
'pto aafakmslfsai'
s[-15:-20:-1]
'ksalf'
s[::-1]
'ipatsaf lqsym ksalf avaj nohtyp'
s[-5::-1]
'saf lqsym ksalf avaj nohtyp'
s[-5:0:-1]
'saf lqsym ksalf avaj nohty'
s[5::-1]
'nohtyp'
s
'python java flask mysql fastapi'
'java' in s
True
'mysql' in s
True
'c++' not in s
True
'python' not in s
False
s
'python java flask mysql fastapi'
len(s)
31
ord('a')
97
ord('c')
99
ord('0')
48
ord('*')
42
ord('+')
43
ord('s')
115
chr(20)
'\x14'
chr(10)
'\n'
max(s)
'y'
s
'python java flask mysql fastapi'
min(s)
' '
sorted(s)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'f', 'f', 'h', 'i', 'j', 'k', 'l', 'l', 'm', 'n', 'o', 'p', 'p', 'q', 's', 's', 's', 't', 't', 'v', 'y', 'y']
t
'programming'
sorted(t)
['a', 'g', 'g', 'i', 'm', 'm', 'n', 'o', 'p', 'r', 'r']
s
'python java flask mysql fastapi'
s.upper()
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.lower()
'python java flask mysql fastapi'
s.swapcase()
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.title()
'Python Java Flask Mysql Fastapi'
s.capatalize()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s.capatalize()
AttributeError: 'str' object has no attribute 'capatalize'. Did you mean '.capitalize' instead of '.capatalize'?
s.capatalize()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s.capatalize()
AttributeError: 'str' object has no attribute 'capatalize'. Did you mean '.capitalize' instead of '.capatalize'?
s.capitalize()
'Python java flask mysql fastapi'
"STRAbbbbbbbbbbbbBBJHYGJDSD".casefold()
'strabbbbbbbbbbbbbbjhygjdsd'
s='python'
s
'python'
s.center(40,'-')
'-----------------python-----------------'
s.center(40,'*')
'*****************python*****************'
s.ljust(40,'*')
'python**********************************'
s.rjust(40,'*')
'**********************************python'
1
1
1
'1'.zfill(5)
'00001'
'123.zfill(5)
SyntaxError: unterminated string literal (detected at line 1)
'123'.zfill(5)
'00123'
'1234567'.zfill(5)
'1234567'
'1234'.zfill(5)
'01234'
'1234567'.zfill(5)/
SyntaxError: invalid syntax
s
'python'
s='python java flask mysql fastapi'
s
'python java flask mysql fastapi'
s.find('z')
-1
s.find('y')
1
s.find('a')
8
s.rfind('a')
28
>>> s.index('f')
12
>>> s.index('f')
12
>>> s.rindex('f')
24
>>> s.find('j')
7
>>> s
'python java flask mysql fastapi'
>>> s.count('a')
5
>>> s.count('y')
2
>>> s.count('h')
1
>>> s.count('z')
0
>>> s = '      codeg   nan        '
>>> s
'      codeg   nan        '
>>> s.strip()
'codeg   nan'
>>> s.lstrip()
'codeg   nan        '
>>> s.rstrip()
'      codeg   nan'
>>> s
'      codeg   nan        '
>>> s='python java flask mysql fastapi'
>>> s
'python java flask mysql fastapi'
>>> s.replace('a','*')
'python j*v* fl*sk mysql f*st*pi'
>>> s.replace('p','1')
'1ython java flask mysql fasta1i'
>>> s.maketrans('apkqs','12345')
{97: 49, 112: 50, 107: 51, 113: 52, 115: 53}
>>> s.traslate(s.maketrans('apkqs','12345'))
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    s.traslate(s.maketrans('apkqs','12345'))
AttributeError: 'str' object has no attribute 'traslate'. Did you mean '.translate' instead of '.traslate'?
>>> s.traslate(s.maketrans('apkqs','12345'))
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    s.traslate(s.maketrans('apkqs','12345'))
AttributeError: 'str' object has no attribute 'traslate'. Did you mean '.translate' instead of '.traslate'?
>>> s.translate(s.maketrans('apkqs','12345'))
'2ython j1v1 fl153 my54l f15t12i'
>>> s.translate(s.maketrans('aeiou','*****'))
'pyth*n j*v* fl*sk mysql f*st*p*'
