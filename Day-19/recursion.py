'''
def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)
'''
'''
def display(n):
    if n>10:
        return
    
    display(n+1)
    print(n)
display(1)
'''
'''
s = 'python programming'
def display(n):
    if n==len(s):
        print()
        return
    print(s[n],end=' ')
    display(n+1)
    print(s[n],end=' ')
display(0)
'''
'''
s = 'python'
def display(n):
    if n==len(s):
        print()
        return
    print(s[0])
    print(s[0:1])
    print(s[0:2])
    print(s[0:3])
    print(s[0:4])
    print(s[0:5])
    print(s[0:6])
display(0)
'''
'''
s = 'python'
def display(n):
    if n==len(s):
        print()
        return
    print(s[:n+1])
    display(n+1)
display(0)
'''
'''
s = 'codegnan'
def display(n,w):
    if n>len(s)-w:
        return
    print(s[n:n+w])
    display(n+1,w)
display(0,4)
'''
'''
def display(n):
    if n < 1:
        return 0
    return n + display(n-1)
print(display(10))
'''
'''
def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))
'''

l = [34,5,567,8,234,7,68,83]
def sumoflst(n):
    if n == len(l):
        return 0
    return l[n]+sumoflst(n+1)

print(sumoflst(0))