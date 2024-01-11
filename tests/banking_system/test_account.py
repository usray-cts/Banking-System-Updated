```python
import pytest
from account import Account

# Unit tests for the Account class

# Scenario 1: Creating an account
def test_create_account_positive_balance():
    account = Account("123456", 1000)
    assert account.account_number == "123456"
    assert account.balance == 1000
    assert account.transactions == []

def test_create_account_zero_balance():
    account = Account("123456", 0)
    assert account.account_number == "123456"
    assert account.balance == 0
    assert account.transactions == []

# Scenario 2: Depositing money
def test_deposit_positive_amount():
    account = Account("123456", 1000)
    new_balance = account.deposit(100, "T1", "2022-01-01 10:00:00")
    assert new_balance == 1100
    assert account.transactions[-1] == {'transaction_id': 'T1', 'type': 'deposit', 'amount': 100, 'timestamp': '2022-01-01 10:00:00'}

def test_deposit_zero_amount():
    account = Account("123456", 1000)
    new_balance = account.deposit(0, "T1", "2022-01-01 10:00:00")
    assert new_balance == 1000
    assert account.transactions[-1] == {'transaction_id': 'T1', 'type': 'deposit', 'amount': 0, 'timestamp': '2022-01-01 10:00:00'}

def test_deposit_negative_amount():
    account = Account("123456", 1000)
    with pytest.raises(ValueError):
        account.deposit(-100, "T1", "2022-01-01 10:00:00")

def test_deposit_non_numeric_value():
    account = Account("123456", 1000)
    with pytest.raises(ValueError):
        account.deposit("100", "T1", "2022-01-01 10:00:00")

# Scenario 3: Withdrawing money
def test_withdraw_less_than_balance():
    account = Account("123456", 1000)
    new_balance = account.withdraw(100, "T2", "2022-01-02 10:00:00")
    assert new_balance == 900
    assert account.transactions[-1] == {'transaction_id': 'T2', 'type': 'withdraw', 'amount': 100, 'timestamp': '2022-01-02 10:00:00'}

def test_withdraw_equal_to_balance():
    account = Account("123456", 1000)
    new_balance = account.withdraw(1000, "T2", "2022-01-02 10:00:00")
    assert new_balance == 0
    assert account.transactions[-1] == {'transaction_id': 'T2', 'type': 'withdraw', 'amount': 1000, 'timestamp': '2022-01-02 10:00:00'}

def test_withdraw_greater_than_balance():
    account = Account("123456", 1000)
    with pytest.raises(ValueError):
        account.withdraw(1100, "T2", "2022-01-02 10:00:00")

def test_withdraw_negative_amount():
    account = Account("123456", 1000)
    with pytest.raises(ValueError):
        account.withdraw(-100, "T2", "2022-01-02 10:00:00")

def test_withdraw_non_numeric_value():
    account = Account("123456", 1000)
    with pytest.raises(ValueError):
        account.withdraw("100", "T2", "2022-01-02 10:00:00")

# Scenario 4: Getting the account statement
def test_get_account_statement_multiple_transactions():
    account = Account("123456", 1000)
    account.deposit(100, "T1", "2022-01-01 10:00:00")
    account.withdraw(100, "T2", "2022-01-02 10:00:00")
    statement = account.get_account_statement()
    assert len(statement) == 2

def test_get_account_statement_one_transaction():
    account = Account("123456", 1000)
    account.deposit(100, "T1", "2022-01-01 10:00:00")
    statement = account.get_account_statement()
    assert len(statement) == 1

def test_get_account_statement_no_transactions():
    account = Account("123456", 1000)
    statement = account.get_account_statement()
    assert statement == []
```
