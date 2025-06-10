from BaseClass import BankAccount
from SavingAct import SavingsAccount
from ChqAct import CheckingAccount

# initial values
savings_account = SavingsAccount(balance = 25, interest_rate = 0.02)
checking_account = CheckingAccount(balance = 5, interest_rate = 0.01)

# report

def sav_report():
    print("Starting Balance: $", round(savings_account._starting_balance, 2))
    print("Total amount of deposits: $", round(savings_account._total_deposits, 2))
    print("Total amount of withdrawals: $", round(savings_account._total_withdrawals, 2))
    print("Service Charges: $", round(savings_account._service_charges, 2))
    print("Current Balance: $", round(savings_account._balance, 2))
    print("Account Status (True if Active, False if Inactive): ", savings_account._active)
    savings_account.close_month()

def check_report():
    print("Starting Balance: $", round(checking_account._starting_balance, 2))
    print("Total amount of deposits: $", round(checking_account._total_deposits, 2))
    print("Total amount of withdrawals: $", round(checking_account._total_withdrawals, 2))
    print("Service Charges: $", round(checking_account._service_charges, 2))
    print("Current Balance: $", round(checking_account._balance, 2))
    print("Account Status (True if Active, False if Inactive):", checking_account._active)
    checking_account.close_month()

# savings menu

def savings_menu():
    print("\nSavings Account Menu\n""A: Deposit\n""B: Withdraw\n""C: Report\n""Q: Return to Bank Menu")
    option = input("Please select an option:").strip().upper()
    # Add logic for savings account operations here based on option
    if option == "A":
        try:
            amount = float(input("Please input an amount to deposit:"))
            savings_account.deposit(amount)
        except ValueError:
            print("Invalid input.")
    elif option == "B":
        try:
            amount = float(input("Please input an amount to withdraw:"))
            savings_account.withdraw(amount)
        except ValueError:
            print("Invalid input.")
    elif option == "C":
        sav_report()
    elif option == "Q":
        main_menu()
    else:
        print("Invalid option.")

# checking menu

def checking_menu():
    print("\nChecking Account Menu\n""A: Deposit\n""B: Withdraw\n""C: Report\n""Q: Return to Bank Menu")
    option = input("Please select an option:").strip().upper()
    # Add logic for checking account operations here based on option
    if option == "A":
        try:
            amount = float(input("Please input an amount to deposit:"))
            checking_account.deposit(amount)
        except ValueError:
            print("Invalid input.")
    elif option == "B":
        try:
            amount = float(input("Please input an amount to withdraw:"))
            checking_account.withdraw(amount)
        except ValueError:
            print("Invalid input.")
    elif option == "C":
        check_report()
    elif option == "Q":
        main_menu()
    else:
        print("Invalid option.")

# main menu

def main_menu():
    while True: # Use a loop to keep the menu running
        print("\nBank Menu\n""A: Savings\n""B: Checking\n""Q: Exit")
        option = input("Please select an option:").strip().upper()

        if option == "A":
            savings_menu()
        elif option == "B":
            checking_menu()
        elif option == "Q":
            print("Thank you for banking with us.")
            break # Exit the loop to end the program
        else:
            print("Invalid option.")

main_menu()
