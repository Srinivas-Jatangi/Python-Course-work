'''
def numbers():
    for i in range(1,11):
        print(i)

numbers()
numbers()
numbers()
'''
'''
def factors(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c>2:
        print("Not Prime number")
    else:
        print("Prime number")

factors(int(input("Enter the number:")))
'''
'''
def factors(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return "Not a prime number"
    return "prime number"
print(factors(int(input("Enter the number: "))))
'''
'''
def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return "Not a prime number"
    return "prime number"
print(isprime(int(input("Enter the number: "))))
'''
'''
def sumofdigs(n):
    sum = 0
    while n>0:
        sum+= n%10
        n//=10

    return sum

print(sumofdigs(34567))
print(sumofdigs(12345))
'''
'''
#reverse number
def revs(n):
    sum=0
    while n>0:
        sum = (sum*10) + n%10
        n//=10
    return sum
print(revs(34567))
print(revs(1234))
'''
'''
def display(name,email,password):
    print("name:",name)
    print("email:",email)
    print("password:",password)
display("abc","abc@gamil.com","abc@123",)
display("abc@gamil.com","abc","abc@123")
display("abc@123","abc","abc@gmail.com")
'''
'''
#positional arguments
def display(name,email,password):
    print("name:",name)
    print("email:",email)
    print("password:",password)
display(name="abc",email="abc@gamil.com",password="abc@123",)
display(email="abc@gamil.com",name="abc",password="abc@123")
display(password="abc@123",name="abc",email="abc@gmail.com")
'''
'''
#default arguments
#default should in last
def display(name,email,password,phonenumber=None):
    print("name:",name)
    print("email:",email)
    print("password:",password)
    print("phonenumber:",phonenumber)
display("abc","abc@gamil.com","abc@123",)
display("abc@gamil.com","abc","abc@123",9823917123)
'''
'''
#variable length argument
#for variable length argument keep single *
def display(*n):
    print(n)

display(1,2,3,4)
display(1,2,3)
display(1,2,3,4,5,6)
'''
'''
#keyword arguments
#for keyword arguments keep double **

def display(**n):
    print(n)

display(n1=1,n2=2,n3=3,n4=4) 
display(n1=1,n2=2)
display(n1=1,n2=2,n3=3)
'''
