import sys
sys.path.insert(0, r'C:\Users\2129823\OneDrive - Cognizant\Documents\Workspace\CapOne Demo\New Bank\banking_system') 

import pytest
from account import Account
from transaction import Transaction
from bank import Bank

# Mocking the classes and their methods as they are not defined in the problem
class MockBank(Bank):
    def create_account(self, account_number):
        if isinstance(account_number, str) and len(account_number) == 8:
            return MockAccount(account_number)
        else:
            return None

class MockAccount(Account):
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def get_account_statement(self):
        return self.balance

class MockTransaction(Transaction):
    def __init__(self, account):
        self.account = account

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.account.balance += amount
            return self.account.balance
        else:
            return "Invalid amount"

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.account.balance:
                self.account.balance -= amount
                return self.account.balance
            else:
                raise ValueError("Insufficient funds")
        else:
            return "Invalid amount"

@pytest.fixture
def bank():
    return MockBank()

@pytest.fixture
def account(bank):
    return bank.create_account("12345678")

@pytest.fixture
def transaction(account):
    return MockTransaction(account)

def test_create_account(bank):
    account = bank.create_account("12345678")
    assert isinstance(account, MockAccount)
    assert account.account_number == "12345678"
    assert account.balance == 0

    account = bank.create_account("invalid")
    assert account is None

def test_deposit(transaction):
    assert transaction.deposit(500) == 500
    assert transaction.deposit(200) == 700
    assert transaction.deposit(-100) == "Invalid amount"
    assert transaction.deposit("invalid") == "Invalid amount"

def test_withdraw(transaction):
    transaction.deposit(500)
    assert transaction.withdraw(200) == 300
    assert transaction.withdraw(300) == 0
    with pytest.raises(ValueError):
        transaction.withdraw(100)
    assert transaction.withdraw(-100) == "Invalid amount"
    assert transaction.withdraw("invalid") == "Invalid amount"

def test_get_account_statement(account, transaction):
    assert account.get_account_statement() == 0
    transaction.deposit(500)
    assert account.get_account_statement() == 500
    transaction.withdraw(200)
    assert account.get_account_statement() == 300

def test_no_account(bank):
    transaction = MockTransaction(None)
    assert transaction.deposit(500) == "Invalid amount"
    assert transaction.withdraw(200) == "Invalid amount"
    assert bank.create_account(None).get_account_statement() is None
