import sys
sys.path.insert(0, r'C:\Users\2129823\OneDrive - Cognizant\Documents\Workspace\CapOne Demo\New Bank\banking_system') 
import pytest
from bank import Bank
from account import Account

class MockAccount:
    def __init__(self, account_number):
        self.account_number = account_number

Bank.Account = MockAccount

def test_create_account():
    bank = Bank()
    account = bank.create_account('12345')
    assert isinstance(account, MockAccount)
    assert account.account_number == '12345'

    with pytest.raises(ValueError, match="Account 12345 already exists."):
        bank.create_account('12345')

def test_get_account():
    bank = Bank()
    bank.create_account('12345')
    account = bank.get_account('12345')
    assert isinstance(account, MockAccount)
    assert account.account_number == '12345'

    with pytest.raises(ValueError, match="Account not found."):
        bank.get_account('67890')

def test_create_account_invalid_input():
    bank = Bank()
    with pytest.raises(ValueError):
        bank.create_account(None)

    with pytest.raises(ValueError):
        bank.create_account([])

def test_get_account_invalid_input():
    bank = Bank()
    with pytest.raises(ValueError):
        bank.get_account(None)

    with pytest.raises(ValueError):
        bank.get_account([])

def test_create_account_empty_input():
    bank = Bank()
    with pytest.raises(ValueError):
        bank.create_account('')

def test_get_account_empty_input():
    bank = Bank()
    with pytest.raises(ValueError):
        bank.get_account('')
