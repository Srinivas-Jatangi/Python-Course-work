data={
    123456:{"Pin":1234,"balance":5000,"transactions":[]},
    123457:{"Pin":1234,"balance":6000,"transactions":[]},
    123458:{"Pin":1234,"balance":7000,"transactions":[]},
    123459:{"Pin":1234,"balance":8000,"transactions":[]}
}

def login():
    global acc_num
    acc_num = int(input("Enter the account number: "))
    Pin = int(input("Enter the Pin: "))
    if acc_num in data and data[acc_num]["Pin"]==Pin:
        print("login Successful")
        return True
    else:
        print("Invalid login")
        return False

def menu():
    print()
    print('[c]heck Balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[T]ransactions')
    print('Change [P]in')
    print('[E]xit')

def checkbalance():
    print(f"Current Balance is {data[acc_num]['balance']}")

def deposit():
    amount = int(input("Enter the amount: "))
    data[acc_num]["balance"]+=amount
    data[acc_num]["transactions"].append(f'Deposit: ${amount}/-')
    print(f"{amount} is deposited successfully")

def withdraw():
    amount = int(input("Enter the amount: "))
    if data[acc_num]["balance"]>= amount:
        data[acc_num]["balance"]-=amount
        data[acc_num]["transactions"].append(f'Withdraw: ${amount}/-')
        print(f"{amount} is Withdraw successfully")
    else:
        print("Insuffiecent Balance")

def transactions():
    if data[acc_num]["transactions"]:
        print("------------Transactional History---------------")
        for i in data[acc_num]["transactions"]:
            print(i)
    else:
        print("No Transactions yet")

def changepin():
    pass