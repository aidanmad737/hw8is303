from hw8functions import BankAccount, display_menu, make_deposit, make_withdrawal, view_account_information


#Main program
#name input, strip() to remove whitespaces
print("Welcome to the Bank of Aidan!")
customer_name = input("Please enter your name: ").strip()

while not customer_name:
    customer_name = input("Name cannot be blank. Please enter your name: ").strip()

account = BankAccount(customer_name)


#User Choice
while True:
    display_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        make_deposit(account)
    elif choice == "2":
        make_withdrawal(account)
    elif choice == "3":
        view_account_information(account)
    elif choice == "4":
        print("Thank you for your business!")
        break
    #break out of loop bc user is quitting
    else:
        print("Invalid choice. Please try again.")