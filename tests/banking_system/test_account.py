```python
import pytest
from account import Account

# Test cases for creating an account
def test_create_account():
    account1 = Account('123456', 1000)
    assert account1.balance == 1000
    account2 = Account('123456', 0)
    assert account2.balance == 0
    account3 = Account('123456')
    assert account3.balance == 0

# Test cases for depositing money
def test_deposit():
    account = Account('123456')
    assert account.deposit(500, 'trans001', '2022-01-01 10:00:00') == 500
    assert account.deposit(0, 'trans002', '2022-01-01 11:00:00') == 500
    with pytest.raises(ValueError):
        account.deposit(-500, 'trans003', '2022-01-01 12:00:00')
    with pytest.raises(ValueError):
        account.deposit('500', 'trans004', '2022-01-01 13:00:00')
    with pytest.raises(ValueError):
        account.deposit(None, 'trans005', '2022-01-01 14:00:00')

# Test cases for withdrawing money
def test_withdraw():
    account = Account('123456', 1500)
    assert account.withdraw(200, 'trans006', '2022-01-02 10:00:00') == 1300
    assert account.withdraw(1300, 'trans007', '2022-01-02 11:00:00') == 0
    with pytest.raises(ValueError):
        account.withdraw(2000, 'trans008', '2022-01-02 12:00:00')
    with pytest.raises(ValueError):
        account.withdraw(-200, 'trans009', '2022-01-02 13:00:00')
    with pytest.raises(ValueError):
        account.withdraw('200', 'trans010', '2022-01-02 14:00:00')
    with pytest.raises(ValueError):
        account.withdraw(None, 'trans011', '2022-01-02 15:00:00')

# Test cases for getting the account statement
def test_get_account_statement():
    account = Account('123456')
    account.deposit(500, 'trans001', '2022-01-01 10:00:00')
    assert len(account.get_account_statement()) == 1
    empty_account = Account('123456')
    assert len(empty_account.get_account_statement()) == 0

# Edge cases for depositing and withdrawing money
def test_edge_cases():
    account = Account('123456')
    assert account.deposit(1e18, 'trans012', '2022-01-03 10:00:00') == 1e18
    assert account.deposit(1e-18, 'trans013', '2022-01-03 11:00:00') == 1e18
    assert account.deposit(123.456789012345, 'trans014', '2022-01-03 12:00:00') == 1e18 + 123.456789012345
    with pytest.raises(ValueError):
        account.withdraw(1e18, 'trans015', '2022-01-04 10:00:00')
    assert account.withdraw(1e-18, 'trans016', '2022-01-04 11:00:00') == 1e18 + 123.456789012345 - 1e-18
    assert account.withdraw(123.456789012345, 'trans017', '2022-01-04 12:00:00') == 1e18
    for i in range(1, 1000001):
        account.deposit(1, f'trans{i:06}', '2022-01-05 10:00:00')
    assert len(account.get_account_statement()) == 1000004
    account.deposit(1e18, 'trans1000001', '2022-01-05 11:00:00')
    account.deposit(1e-18, 'trans1000002', '2022-01-05 12:00:00')
    assert len(account.get_account_statement()) == 1000006

# Edge cases for creating an account
def test_create_account_edge_cases():
    account1 = Account('123456', 1e18)
    assert account1.balance == 1e18
    account2 = Account('123456', 1e-18)
    assert account2.balance == 1e-18
    account3 = Account('123456', 123.456789012345)
    assert account3.balance == 123.456789012345
```