import time
import json

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0, password=""):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.password = password

    def deposit(self, amount):
        if amount > 0:
            print("Depositing funds...", end=" ")
            for _ in range(3):  # Display loading dots
                print(".", end="", flush=True)
                time.sleep(1)
            self.balance += amount
            print(f"\nDeposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            print("Withdrawing funds...", end=" ")
            for _ in range(3):  # Display loading dots
                print(".", end="", flush=True)
                time.sleep(1)
            self.balance -= amount
            print(f"\nWithdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        print(f"Account Balance for {self.account_holder}: ${self.balance}")

def save_accounts(accounts):
    with open("accounts.json", "w") as file:
        account_data = []
        for account_number, account in accounts.items():
            account_data.append({
                "account_number": account_number,
                "account_holder": account.account_holder,
                "balance": account.balance,
                "password": account.password,
            })
        json.dump(account_data, file)

def load_accounts():
    try:
        with open("accounts.json", "r") as file:
            account_data = json.load(file)
            accounts = {}
            for data in account_data:
                account = BankAccount(data["account_number"], data["account_holder"], data["balance"], data["password"])
                accounts[data["account_number"]] = account
            return accounts
    except FileNotFoundError:
        return {}

def main():
    accounts = load_accounts()  # Load existing accounts from the JSON file

    while True:
        print("\nBank System Menu:")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                print("Account already exists.")
            else:
                account_holder = input("Enter account holder name: ")
                password = input("Set a password for the account: ")
                new_account = BankAccount(account_number, account_holder, password=password)
                accounts[account_number] = new_account
                print(f"Account created for {account_holder} with account number {account_number}.")
                save_accounts(accounts)  # Save the updated account data

        elif choice == "2":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                password = input("Enter the account password: ")
                if accounts[account_number].password == password:
                    print(f"Accessing account for {accounts[account_number].account_holder}.")
                    while True:
                        print("\nAccount Menu:")
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Check Balance")
                        print("4. Back to Main Menu")

                        sub_choice = input("Enter your choice: ")

                        if sub_choice == "1":
                            amount = float(input("Enter deposit amount: "))
                            accounts[account_number].deposit(amount)
                            save_accounts(accounts)  # Save the updated account data
                        elif sub_choice == "2":
                            amount = float(input("Enter withdrawal amount: "))
                            accounts[account_number].withdraw(amount)
                            save_accounts(accounts)  # Save the updated account data
                        elif sub_choice == "3":
                            accounts[account_number].get_balance()
                        elif sub_choice == "4":
                            break
                        else:
                            print("Invalid choice. Please try again.")

                else:
                    print("Incorrect password. Access denied.")
            else:
                print("Account not found.")

        elif choice == "3":
            print("Exiting the bank system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
