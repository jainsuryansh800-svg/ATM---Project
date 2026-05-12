balance = int(1000)
pin = int(input("Create Your Pin : "))
User = int(input(" Enter Your Pin : "))


if User == pin:
    print(" Welcome ")
    while True:
        print("/n ATM Menu ")
        print("1. Deposit ")
        print("2. Check Balance ")
        print("3. Withdrawl ")
        print("4. Exit ")

        choice = int(input(" Write Your Choice : "))
        if choice == 1:
            amount = float(input(" Enter Deposited Amount : "))
            if amount <= 0:
                print(" Invalid Transaction , Try Again ")
                continue
            balance += amount
            print(f" Amount Diposited Successfully. Current balance : Rs. {balance:.2f}")

        elif choice == 2:
            print(f" Current Balance : Rs. {balance:.2f}")

        elif choice == 3:
            decrease = float(input(" Write Your Amount : "))
            if decrease >= balance:
                print(" Invalid Transaction! . Try Again ")
                continue
            balance -= decrease
            print(f" Amount Withdrawled Successfully . Current Balance : Rs. {balance:.2f}")
            
        elif choice == 4:
            print(" Visit Again ")
            break        
        else:
            print(" Invalid Choice ")
            break


else:
    print("Incorrect PIN")