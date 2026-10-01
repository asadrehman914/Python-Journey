correct_pin="1234"
balance=50000

pin=input("Enter the pin: ")
if pin != correct_pin:
    print("Invalid Pin")
    exit()
if pin == correct_pin:
    print("---ATM MENU---")
    print("1.Widthdrawal")
    print("2.Deposit")
    print("3.Check Balance")
    print("4.Exit")

choice=input("Enter Your Choice: ")
match choice:
    case "1":
        print("Amount can be widthraw in 500,1000,5000 Pattern you can't enter e.g 600")
        amount=float(input("Enter Amount: "))
        if amount <=0:
            print("Invalid Amount")
        elif amount>balance:
            print("Infcient Balance")
        else:
            balance -= amount
            print("Widthrawal Sucessful")
            print("Remaning Balance",balance)
    case "2":
        amount=float(input("Enter Deposit Amount: "))
        if amount <= 0:
            print("Invalid Deposit Amount")
        else:
            balance += amount
            print("Your Balance ",balance)
    case "3":
        print("Your Balance",balance)
    case 4:
        print("Thanks For Using The ATM")
    case _:
        print("Invalid Choice")



