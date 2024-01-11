import sys
sys.path.insert(0, r'C:\Users\2129823\OneDrive - Cognizant\Documents\Workspace\CapOne Demo\New Bank\banking_system') 

import pytest
import uuid
from datetime import datetime
from account import Account
from transaction import Transaction
from unittest.mock import MagicMock

# Mocking the Account class
class MockAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount, transaction_id, timestamp):
        self.balance += amount
        return self.balance

    def withdraw(self, amount, transaction_id, timestamp):
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance

# Testing the deposit method
def test_deposit():
    account = MockAccount()
    transaction = Transaction(account)

    # Positive deposit amount
    response = transaction.deposit(100)
    assert response["status"] == "success"
    assert response["new_balance"] == 100

    # Zero deposit amount
    response = transaction.deposit(0)
    assert response["status"] == "success"
    assert response["new_balance"] == 100

    # Negative deposit amount
    with pytest.raises(ValueError):
        transaction.deposit(-100)

# Testing the withdraw method
def test_withdraw():
    account = MockAccount()
    account.balance = 100
    transaction = Transaction(account)

    # Positive withdrawal amount
    response = transaction.withdraw(50)
    assert response["status"] == "success"
    assert response["new_balance"] == 50

    # Zero withdrawal amount
    response = transaction.withdraw(0)
    assert response["status"] == "success"
    assert response["new_balance"] == 50

    # Negative withdrawal amount
    with pytest.raises(ValueError):
        transaction.withdraw(-50)

    # Withdrawal amount greater than account balance
    response = transaction.withdraw(101)
    assert response["status"] == "failed"
    assert "Insufficient balance." in response["error"]

# Testing deposit and withdrawal in quick succession
def test_quick_succession():
    account = MockAccount()
    transaction = Transaction(account)

    # Deposit an amount, then immediately withdraw the same amount
    response = transaction.deposit(100)
    assert response["status"] == "success"
    assert response["new_balance"] == 100

    response = transaction.withdraw(100)
    assert response["status"] == "success"
    assert response["new_balance"] == 0

# Testing multiple deposits and withdrawals in quick succession
def test_multiple_transactions():
    account = MockAccount()
    transaction = Transaction(account)

    # Make multiple deposits and withdrawals in a random order, with varying amounts
    response = transaction.deposit(100)
    assert response["status"] == "success"
    assert response["new_balance"] == 100

    response = transaction.withdraw(50)
    assert response["status"] == "success"
    assert response["new_balance"] == 50

    response = transaction.deposit(200)
    assert response["status"] == "success"
    assert response["new_balance"] == 250

    response = transaction.withdraw(100)
    assert response["status"] == "success"
    assert response["new_balance"] == 150
