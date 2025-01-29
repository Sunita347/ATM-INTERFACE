import time

User_Id = int(input("Enter your Account Number:"))
print("Your User_ID:", User_Id)
time.sleep(2)
password = 1234
pin = int(input("Enter your ATM pin :"))
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")
Balance = 5000

if pin == password:
    while True:
        print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == transfer money
            5 == exit""")
        try:
            print("\n")
            option = int(input("Enter your choice : "))
        except:
            print("Invalid option ")
        if option == 1:
            print("Current Balance: ", Balance)
            print("------------------------------------------------------------------------------------------------")
            print("------------------------------------------------------------------------------------------------")
        elif option == 2:
            withdraw_amount = int(input("Please enter withdraw_amount:"))
            if Balance>=withdraw_amount:
                Balance = (Balance - withdraw_amount)
                print("------------------------------------------------------------------------------------------------")
                print("------------------------------------------------------------------------------------------------")
                print(f"{withdraw_amount} is debited from your account")
                print("------------------------------------------------------------------------------------------------")
                print(f"Your Updated Balance :", Balance)
                print("------------------------------------------------------------------------------------------------")
                print("------------------------------------------------------------------------------------------------")
            else:
                print("Insufficient Balance")
        elif option == 3:
            deposit_amount = int(input("Please Enter your deposit_amount:"))
            Balance = (Balance + deposit_amount)
            print("------------------------------------------------------------------------------------------------")
            print("------------------------------------------------------------------------------------------------")
            print(f"{deposit_amount} is credited in your account")
            print("------------------------------------------------------------------------------------------------")
            print(f"Your Updated Balance:", Balance)
            print("------------------------------------------------------------------------------------------------")
            print("------------------------------------------------------------------------------------------------")
        elif option == 4:
            transfer_amount = int(input("Please enter the amount to transfer: "))
            if Balance >= transfer_amount:
                recipient_account = int(input("Enter the recipient's account number: "))
                Balance -= transfer_amount
                print("------------------------------------------------------------------------------------------------")
                print("------------------------------------------------------------------------------------------------")
                print(f"{transfer_amount} has been transferred to account {recipient_account}")
                print("------------------------------------------------------------------------------------------------")
                print(f"Your Updated Balance: {Balance}")
                print("------------------------------------------------------------------------------------------------")
                print("------------------------------------------------------------------------------------------------")
            else:
                print("Insufficient Balance")
                print("------------------------------------------------------------------------------------------------")
                print("------------------------------------------------------------------------------------------------")
        elif option == 5:
            print("Exit")
            print("------------------------------------------------------------------------------------------------")
            print("------------------------------------------------------------------------------------------------")
            break
else:
    print("Wrong pin please try again")
