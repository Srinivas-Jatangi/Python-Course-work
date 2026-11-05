'''
#int
#while cond:
    #stmt
    #upd
l=[1,0,3,0,4,0,0,0,0,5,0,6,0,4,0]
while 0 in l:
    l.remove(0)

print(l)
'''
'''
i=1
while i<11:
    print(i)
    i+=1
    '''
'''
i=10
while i>0:
    print(i)
    i-=1
    '''
'''
i=2
while i<101:
    print(i)
    i+=2
    '''
'''
i=5
while i<11:
    print(i)
    i+=5
    '''
'''
a = 'python programming'
i=0
while i<len(a):
    print(i)
    i+=1
    '''
'''
a = 'python programming'
i=0
while i<len(a):
    print(i,a[i])
    i+=1
    '''
'''
a = [1,3,5,6,7,8,9]
i=0
while i<len(a):
    print(i,a[i])
    i+=1
    '''
'''
a = [1,3,5,6,7,8,9]
i=0
while i<len(a)-1:
    i+=1
    if a[i]==5:
        continue
    print(i,a[i])
    '''

c='pythonprogramming'
i=0
j=len(c)-1
while i<=j:
    if i==j:
        print(c[i])
    else:
        print(c[i],c[j])
    i+=1
    j-=1