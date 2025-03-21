"""Create a python class called BankAccount with attributes like account_number, balance, 
date_of_opening and customer_name, and methods like deposit, withdraw, 
check_balance and customer_details
i. The deposit method should return the amount deposited 
ii. The withdraw method return insufficient balance if account balance is less than amount to 
be withdrawn else it should return the amount that has been withdrawn.
iii. The check_balance method should print the current balance.
iv. The customer_details method should print customer name, account number, date of 
account opening and balance
Create an instance of the BankAccount class to represent a bank account. Perform the 
following operations: make a deposit, withdraw funds, and display the account information 
for the created bank account instance."""
class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance  # Default balance is 0 unless specified

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Withdrawn: {amount}"

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")

# Creating an instance of BankAccount
account1 = BankAccount("203256", "shalom omamo", "2025-03-21", 1000)

# Performing operations to deposit,withdraw and try to wwithdraw more
print(account1.deposit(500)) 
print(account1.withdraw(200)) 
print(account1.withdraw(2000))  

# Checking balance and displaying details
account1.check_balance()
account1.customer_details()
