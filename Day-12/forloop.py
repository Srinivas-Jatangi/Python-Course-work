'''
#str list tuple set dict range()

#for i in seq:
    #stmt

s = 'codegnan'
for i in s:
    print(i)

a = input("Enter the word: ")
for i in a:
    if i in 'aeiouAEIOU':
        print(i)
        '''
'''
s =(10,23,45,89,56,34,85,12)
for i  in s:
    print(i)

a = list(map(int,input("Enter the nums:" ).split()))
for i in a:
    if i%2==0:
        print(i)
        '''
'''
sumoftuple =0
a = tuple(map(int,input("Enter the nums: ").split()))
for i in a:
    sumoftuple+=i

print("sum of tuple:",sumoftuple)
'''
'''
max = 0
a = set(map(int,input("Enter the nums: ").split()))
for i in a:
    if i>max:
        max = i

print("max of set:",max)
'''
'''
marks = {'python':90,'mysql':85,'fastapi':80,'html':85,'css':90}
for i in marks:
    print(i,marks[i])

sum = 0
marks = {'python':90,'mysql':85,'fastapi':80,'html':85,'css':90}
for i in marks:
    sum += marks[i]

print("Total Marks:",sum)
'''
'''
#range (start,end+1,step)
#range(0,,1)

for i in range(1,11):
    print(i,end='  ')

for i in range(20,0,-1):
    print(i,end='  ')

for i in range(2,101,2):
    print(i,end='  ')
    '''
'''
n = int(input("Enter the table no: "))

for i in range(1,21):
    print(f'{n}*{i}={n*i}')
    '''
'''
#codegnan
#c0o1d2e3g4n5a6n7

c = 'codegnan'
for i in range(len(c)):
    print(c[i],i,end=' ')
    '''
'''
#[12,34,45,10,78,43,80]
#0+1+3+4+6  =14

sum = 0
c = [12,34,45,10,78,43,80]
for i in range(len(c)):
    if c[i]%2==0:
        sum+=i

print(sum)
'''
'''
#[12,34,45,10,78,43,80]
#2*5 = 10

sum = 0
c = [12,34,45,10,78,43,80]
for i in range(len(c)):
    if c[i]%1==0:
        sum-=i
print(sum)
'''
'''
for i in range(1,11):
    if i == 5:
        break
    
print(i)

for i in range(1,11):
    if i == 5:
        continue
    print(i)
    '''

for i in range(1,10):
    pass

if True:
    pass

class Booking:
    pass

def func():
    pass
