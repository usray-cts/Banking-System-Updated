```python
import pytest
from account import Account

# Unit tests for Account class

# Test account initialization
def test_account_initialization():
    # Test initialization with positive balance
    account = Account('123', 100)
    assert account.account_number == '123'
    assert account.balance == 100

    # Test initialization with zero balance
    account = Account('123', 0)
    assert account.account_number == '123'
    assert account.balance == 0

    # Test initialization with negative balance
    with pytest.raises(ValueError):
        account = Account('123', -100)

# Test deposit method
def test_deposit():
    account = Account('123', 100)

    # Test depositing a positive amount
    account.deposit(100, '001', '2022-01-01')
    assert account.balance == 200

    # Test depositing a zero amount
    account.deposit(0, '002', '2022-01-02')
    assert account.balance == 200

    # Test depositing a negative amount
    with pytest.raises(ValueError):
        account.deposit(-100, '003', '2022-01-03')

    # Test depositing a non-numeric amount
    with pytest.raises(ValueError):
        account.deposit('100', '004', '2022-01-04')

# Test withdraw method
def test_withdraw():
    account = Account('123', 200)

    # Test withdrawing an amount less than the balance
    account.withdraw(100, '001', '2022-01-01')
    assert account.balance == 100

    # Test withdrawing an amount equal to the balance
    account.withdraw(100, '002', '2022-01-02')
    assert account.balance == 0

    # Test withdrawing an amount greater than the balance
    with pytest.raises(ValueError):
        account.withdraw(100, '003', '2022-01-03')

    # Test withdrawing a zero amount
    account.withdraw(0, '004', '2022-01-04')
    assert account.balance == 0

    # Test withdrawing a negative amount
    with pytest.raises(ValueError):
        account.withdraw(-100, '005', '2022-01-05')

    # Test withdrawing a non-numeric amount
    with pytest.raises(ValueError):
        account.withdraw('100', '006', '2022-01-06')

# Test get_account_statement method
def test_get_account_statement():
    account = Account('123', 200)

    # Test retrieving the statement of an account with transactions
    account.deposit(100, '001', '2022-01-01')
    account.withdraw(50, '002', '2022-01-02')
    transactions = account.get_account_statement()
    assert len(transactions) == 2

    # Test retrieving the statement of an account without transactions
    account = Account('123', 200)
    transactions = account.get_account_statement()
    assert len(transactions) == 0
```