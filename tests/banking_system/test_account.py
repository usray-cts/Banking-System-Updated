import sys
sys.path.insert(0, r'C:\Users\2129823\OneDrive - Cognizant\Documents\Workspace\CapOne Demo\New Bank\banking_system') 

import pytest
from account import Account

def test_account_creation():
    # Creating an account with a positive initial balance
    acc = Account('123456', 100)
    assert acc.balance == 100
    assert acc.account_number == '123456'
    assert acc.transactions == []

    # Creating an account with no initial balance (default to 0)
    acc = Account('123456')
    assert acc.balance == 0
    assert acc.account_number == '123456'
    assert acc.transactions == []

    # Creating an account with a negative initial balance (should raise an error)
    with pytest.raises(ValueError):
        Account('123456', -100)

def test_deposit_transactions():
    acc = Account('123456')

    # Depositing a positive integer amount
    acc.deposit(100, 'T1', '2022-01-01')
    assert acc.balance == 100

    # Depositing a positive float amount
    acc.deposit(100.5, 'T2', '2022-01-02')
    assert acc.balance == 200.5

    # Depositing a zero amount
    acc.deposit(0, 'T3', '2022-01-03')
    assert acc.balance == 200.5

    # Depositing a negative amount (should raise an error)
    with pytest.raises(ValueError):
        acc.deposit(-100, 'T4', '2022-01-04')

    # Depositing a non-numeric amount (should raise an error)
    with pytest.raises(ValueError):
        acc.deposit("one hundred", 'T5', '2022-01-05')

def test_withdrawal_transactions():
    acc = Account('123456', 100)

    # Withdrawing an amount less than the balance
    acc.withdraw(50, 'T1', '2022-01-01')
    assert acc.balance == 50

    # Withdrawing an amount equal to the balance
    acc.withdraw(50, 'T2', '2022-01-02')
    assert acc.balance == 0

    # Withdrawing an amount greater than the balance (should raise an error)
    with pytest.raises(ValueError):
        acc.withdraw(200, 'T3', '2022-01-03')

    # Withdrawing a negative amount (should raise an error)
    with pytest.raises(ValueError):
        acc.withdraw(-50, 'T4', '2022-01-04')

    # Withdrawing a non-numeric amount (should raise an error)
    with pytest.raises(ValueError):
        acc.withdraw("fifty", 'T5', '2022-01-05')

def test_account_statement():
    acc = Account('123456', 100)

    # Getting the account statement with no transactions (should return an empty list)
    assert acc.get_account_statement() == []

    # Getting the account statement with one transaction
    acc.deposit(100, 'T1', '2022-01-01')
    assert len(acc.get_account_statement()) == 1

    # Getting the account statement with multiple transactions
    acc.deposit(100, 'T2', '2022-01-02')
    acc.withdraw(50, 'T3', '2022-01-03')
    assert len(acc.get_account_statement()) == 3

def test_edge_cases():
    acc = Account('123456', 100)

    # Making a deposit immediately followed by a withdrawal of the same amount
    acc.deposit(100, 'T1', '2022-01-01')
    acc.withdraw(100, 'T2', '2022-01-01')
    assert acc.balance == 100

    # Making a withdrawal immediately followed by a deposit of the same amount
    acc.withdraw(50, 'T3', '2022-01-02')
    acc.deposit(50, 'T4', '2022-01-02')
    assert acc.balance == 100

    # Making multiple deposits and withdrawals in a short period of time
    acc.deposit(100, 'T5', '2022-01-03')
    acc.withdraw(50, 'T6', '2022-01-03')
    acc.deposit(100, 'T7', '2022-01-03')
    acc.withdraw(50, 'T8', '2022-01-03')
    assert acc.balance == 200

    # Making a deposit or withdrawal with a very large amount
    acc.deposit(1000000, 'T9', '2022-01-04')
    assert acc.balance == 1000200

    # Making a deposit or withdrawal with a very small amount (e.g. 0.01)
    acc.deposit(0.01, 'T10', '2022-01-05')
    assert acc.balance == 1000200.01
