class BankAccount:
    def __init__(self, account_number, customer_name, balance, date_of_opening):
        # Store account details
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        # Add money to the balance
        self.balance += amount
        return f"You deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        # Check if there is enough money to withdraw
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"You withdrew {amount}. New balance: {self.balance}"

    def check_balance(self):
        # Print the current balance
        print(f"Your balance is {self.balance}")

    def customer_details(self):
        # Print customer details
        print(f"Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Opened on: {self.date_of_opening}")
        print(f"Balance: {self.balance}")

# Example Usage
account = BankAccount(987654, "Grace Omamo", 2000, "2025-02-01")

print(account.deposit(1000))  
print(account.withdraw(500))  
account.check_balance()       
account.customer_details()    

