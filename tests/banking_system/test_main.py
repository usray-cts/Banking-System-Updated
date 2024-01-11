```python
import pytest
from unittest.mock import Mock, patch
from account import Account
from transaction import Transaction
from bank import Bank

@patch('bank.Bank')
@patch('transaction.Transaction')
@patch('account.Account')
def test_main(mock_account, mock_transaction, mock_bank):
    # Mocking the Bank, Transaction, and Account classes
    mock_bank.create_account.return_value = mock_account
    mock_transaction.return_value = mock_transaction

    # Importing the main.py module
    import main

    # Test: Account Creation
    mock_bank.create_account.assert_called_once_with("12345678")
    assert isinstance(main.account, Account)

    # Test: Deposit Transactions
    mock_transaction.deposit.assert_called_once_with(500)

    # Test: Withdrawal Transactions
    mock_transaction.withdraw.assert_any_call(200)
    mock_transaction.withdraw.assert_any_call(400)

    # Test: Account Statement
    mock_account.get_account_statement.assert_called_once()

    # Test: Exception Handling
    mock_transaction.withdraw.side_effect = ValueError("Insufficient funds")
    with pytest.raises(ValueError) as e:
        main.transaction.withdraw(400)
    assert str(e.value) == "Insufficient funds"

@patch('bank.Bank')
@patch('transaction.Transaction')
@patch('account.Account')
def test_invalid_account_number(mock_account, mock_transaction, mock_bank):
    # Mocking the Bank, Transaction, and Account classes
    mock_bank.create_account.return_value = None
    mock_transaction.return_value = mock_transaction

    # Importing the main.py module
    import main

    # Test: Invalid Account Number
    with pytest.raises(TypeError):
        main.bank.create_account("")

@patch('bank.Bank')
@patch('transaction.Transaction')
@patch('account.Account')
def test_invalid_deposit(mock_account, mock_transaction, mock_bank):
    # Mocking the Bank, Transaction, and Account classes
    mock_bank.create_account.return_value = mock_account
    mock_transaction.return_value = mock_transaction

    # Importing the main.py module
    import main

    # Test: Invalid Deposit
    with pytest.raises(ValueError):
        main.transaction.deposit(-100)
    with pytest.raises(TypeError):
        main.transaction.deposit("abc")

@patch('bank.Bank')
@patch('transaction.Transaction')
@patch('account.Account')
def test_invalid_withdrawal(mock_account, mock_transaction, mock_bank):
    # Mocking the Bank, Transaction, and Account classes
    mock_bank.create_account.return_value = mock_account
    mock_transaction.return_value = mock_transaction

    # Importing the main.py module
    import main

    # Test: Invalid Withdrawal
    with pytest.raises(ValueError):
        main.transaction.withdraw(-100)
    with pytest.raises(TypeError):
        main.transaction.withdraw("abc")
```
