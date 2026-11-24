import logic as lg

if lg.login():
    print("Welcome to the SmartATM")
    while True:
        lg.menu()
        ch = input("Enter the choice: ").upper()

        if ch == 'C':
            lg.checkbalance()
        elif ch == 'D':
            lg.deposit()
        elif ch == 'W':
            lg.withdraw()
        elif ch == 'T':
            lg.transactions()
        elif ch == 'P':
            pass
        elif ch == 'E':
            print("Thankyou, Visit Again")
            break