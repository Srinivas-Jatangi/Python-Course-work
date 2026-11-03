'''
product = input("Enter the product: ")
bestseller = eval(input("Enter the status: "))

if bestseller:
    print(f'{product}is best seller.')
    '''
'''
batterycharge = int(input("Enter the battery: "))

if batterycharge<20:
    print(f'Battery is low: {batterycharge}, charge your phone')
    '''
bill = int(input("Enter the bill: "))
status = eval(input("Is it raining? "))

if status:
    bill+=30
    print("Extra Delivery charges applied")

print(f"Final Bill: {bill}")
