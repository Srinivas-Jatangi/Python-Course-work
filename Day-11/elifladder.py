print("Welcome to the weekend Planner")
budget = int(input("Enter the budget: "))

print("You can go for",end=' ')
if budget > 10000:
    print("Trip")
elif budget > 5000:
    print("Resort")
elif budget > 2000:
    print("cafe")
elif budget > 1000:
    print("movie")
elif budget > 500:
    print("street shopping")
else:
    print("sleep")
    

