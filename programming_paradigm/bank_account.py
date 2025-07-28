# Script to manage a simple bank account with deposit, withdraw, and balance display functionalities.

# class for BankAccount
class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    # Method to withdraw money from the account    
    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    # Method to display the current balance
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")