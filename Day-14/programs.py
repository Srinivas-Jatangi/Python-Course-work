'''
l=[12,9,3,4,5,10,2,4,5,2,4,5]

17
13
5
9
7
10

i = 0
j = len(l)-1

while i<=j:
    if i==j:
        print(l[i])
    else:

        print(l[i]+l[j])
    i+=1
    j-=1
    '''
'''
bill = 0

while True:
    product = input("Enter the product name(STOP): ")
    if product == 'STOP':
        print("Total Bill:",bill)
        break
    price = int(input("Enter the price: "))
    qua = int(input("Enter the quantity: "))
    bill+=price*qua
    '''
products = {
    'sugar':40,
    'salt':30,
    'cooking oil':120,
    'bread':40,
    'butter':60,
    'milk':30,
    'rice':150,
    'wheat':120,
    'jam':40
}

#Display Menu
print("Welcome to the store".center(50,'-'))
print("product Name",'price')
for i in products:
    print(i.ljust(12,' '),':',products[i])

carts = {}
while True:
    cart = input("Enter the Product Name(exit): ").lower()
    if cart == 'exit':
        break
    qua = int(input("Enter the quantity: "))
    carts[cart]=qua


print("Bill".center(50,'-'))
print('Product Name Quantity ($)Price')
bill=0
for i in carts:
    print(i.ljust(12,' '),str(carts[i]).ljust(12,' '),products[i])
    bill += carts[i]*products[i]

print(f"Total bill: ${bill}")
print("Thanks for shopping")







            
