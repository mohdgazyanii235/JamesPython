print("Hello there, you have reached test bank")
print("press")
print("1: If you want to reach the payments helpline")
print("2: If you want to reach the banking helpline")
choice = int(input("Which option: "))
if choice == 1:
    print("1: If you are worried about an incoming payment")
    print("2: If you are worried about an outgoing payment")
    choice = int(input("What is your choice: "))
    if choice == 1:
        print("You've chosen 1")
    elif choice == 2:
        print("You've chosen 2")
    else:
        print("That is not a valid option")
elif choice == 2:
    print("1: Are you concerned about a security issue")
    print("2: Are you trying to make a withdrawl")
    choice = int(input("Do you choose 1 or 2"))
    if choice == 1:
        print("You've chosen option 1")
    elif choice == 2:
        print("You've chosen 2")
    else:
        print("That is not a valid option")
else:
    print("That is not a valid option")