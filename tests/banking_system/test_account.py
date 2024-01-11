```python
import pytest
from account import Account

# Unit tests for Account Initialization
def test_account_initialization_positive_balance():
    account = Account(123456, 100)
    assert account.account_number == 123456
    assert account.balance == 100
    assert account.transactions == []

def test_account_initialization_zero_balance():
    account = Account(123456)
    assert account.account_number == 123456
    assert account.balance == 0
    assert account.transactions == []

def test_account_initialization_negative_balance():
    with pytest.raises(ValueError):
        Account(123456, -100)

# Unit tests for Deposit Transaction
def test_deposit_positive_integer():
    account = Account(123456)
    account.deposit(100, 'T1', '2022-01-01')
    assert account.balance == 100

def test_deposit_positive_float():
    account = Account(123456)
    account.deposit(100.50, 'T1', '2022-01-01')
    assert account.balance == 100.50

def test_deposit_zero():
    account = Account(123456)
    account.deposit(0, 'T1', '2022-01-01')
    assert account.balance == 0

def test_deposit_negative():
    account = Account(123456)
    with pytest.raises(ValueError):
        account.deposit(-100, 'T1', '2022-01-01')

def test_deposit_non_numeric():
    account = Account(123456)
    with pytest.raises(ValueError):
        account.deposit('one hundred', 'T1', '2022-01-01')

# Unit tests for Withdraw Transaction
def test_withdraw_positive_integer():
    account = Account(123456, 200)
    account.withdraw(100, 'T1', '2022-01-01')
    assert account.balance == 100

def test_withdraw_positive_float():
    account = Account(123456, 200)
    account.withdraw(100.50, 'T1', '2022-01-01')
    assert account.balance == 99.50

def test_withdraw_zero():
    account = Account(123456, 200)
    account.withdraw(0, 'T1', '2022-01-01')
    assert account.balance == 200

def test_withdraw_negative():
    account = Account(123456, 200)
    with pytest.raises(ValueError):
        account.withdraw(-100, 'T1', '2022-01-01')

def test_withdraw_non_numeric():
    account = Account(123456, 200)
    with pytest.raises(ValueError):
        account.withdraw('one hundred', 'T1', '2022-01-01')

def test_withdraw_amount_greater_than_balance():
    account = Account(123456, 200)
    with pytest.raises(ValueError):
        account.withdraw(300, 'T1', '2022-01-01')

# Unit tests for Get Account Statement
def test_get_account_statement_no_transactions():
    account = Account(123456)
    assert account.get_account_statement() == []

def test_get_account_statement_one_transaction():
    account = Account(123456)
    account.deposit(100, 'T1', '2022-01-01')
    assert len(account.get_account_statement()) == 1

def test_get_account_statement_multiple_transactions():
    account = Account(123456)
    account.deposit(100, 'T1', '2022-01-01')
    account.deposit(50, 'T2', '2022-01-02')
    assert len(account.get_account_statement()) == 2
```