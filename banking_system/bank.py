
from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number):
        if account_number is None:
            raise ValueError("Account number cannot be None.")
        if not isinstance(account_number, str):
            raise ValueError("Account number must be a string.")
        if account_number in self.accounts:
            raise ValueError(f"Account {account_number} already exists.")
        self.accounts[account_number] = Account(account_number)
        return self.accounts[account_number]

    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_number]
