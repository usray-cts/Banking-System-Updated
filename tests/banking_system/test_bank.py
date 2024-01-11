import pytest
from unittest.mock import patch, MagicMock
from account import Account
from bank import Bank

# Mocking Account class
@patch('bank.Account', autospec=True)
def test_create_account_with_valid_input(mock_account):
    # Creating Bank object
    bank = Bank()
    # Creating mock account object
    mock_account.return_value = MagicMock(spec=Account)
    # Testing with valid account number
    assert bank.create_account("123456") == mock_account.return_value
    assert bank.create_account("ABCDEF") == mock_account.return_value

@patch('bank.Account', autospec=True)
def test_create_account_with_invalid_input(mock_account):
    bank = Bank()
    mock_account.return_value = MagicMock(spec=Account)
    # Testing with invalid account number
    with pytest.raises(ValueError):
        bank.create_account(123456)
    with pytest.raises(ValueError):
        bank.create_account(None)
    with pytest.raises(ValueError):
        bank.create_account(["123456"])

@patch('bank.Account', autospec=True)
def test_create_account_that_already_exists(mock_account):
    bank = Bank()
    mock_account.return_value = MagicMock(spec=Account)
    bank.create_account("123456")
    # Testing with already existing account number
    with pytest.raises(ValueError):
        bank.create_account("123456")
    bank.create_account("ABCDEF")
    with pytest.raises(ValueError):
        bank.create_account("ABCDEF")

@patch('bank.Account', autospec=True)
def test_get_account_that_exists(mock_account):
    bank = Bank()
    mock_account.return_value = MagicMock(spec=Account)
    bank.create_account("123456")
    # Testing with existing account number
    assert bank.get_account("123456") == mock_account.return_value
    bank.create_account("ABCDEF")
    assert bank.get_account("ABCDEF") == mock_account.return_value

@patch('bank.Account', autospec=True)
def test_get_account_that_does_not_exist(mock_account):
    bank = Bank()
    mock_account.return_value = MagicMock(spec=Account)
    # Testing with non-existing account number
    with pytest.raises(ValueError):
        bank.get_account("123456")
    with pytest.raises(ValueError):
        bank.get_account("ABCDEF")

@patch('bank.Account', autospec=True)
def test_edge_cases(mock_account):
    bank = Bank()
    mock_account.return_value = MagicMock(spec=Account)
    # Testing with edge cases
    with pytest.raises(ValueError):
        bank.create_account("")
    with pytest.raises(ValueError):
        bank.create_account(" ")
    with pytest.raises(ValueError):
        bank.create_account("123\n456")