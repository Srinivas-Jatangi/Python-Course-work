'''
#local scope is inside loop
#global  decalaration is we can get both in and out
#non local is only to change the outside one 
#bulid scope

def display():
    global n 
    n=10
    print("inside:",n)

display()
print("outside:",n)
'''
'''
def display():
    course = "JFS"
    print("Starting:",course)
    def update():
        nonlocal course
        course = "PFS"
        print("Updated:",course)
    update()
    print("final:",course)

display()
'''
'''
s ="codegnan"

len = 10

print(max(s))
'''

