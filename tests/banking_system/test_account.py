import pytest
from account import Account

# Test class for Account
class TestAccount:

    # Test for __init__ method
    def test_init(self):
        # Creating an account with a positive balance
        account = Account(123456, 100)
        assert account.account_number == 123456
        assert account.balance == 100

        # Creating an account with a zero balance
        account = Account(123456)
        assert account.account_number == 123456
        assert account.balance == 0

        # Creating an account with a negative balance should raise ValueError
        with pytest.raises(ValueError):
            Account(123456, -100)

    # Test for deposit method
    def test_deposit(self):
        account = Account(123456)

        # Depositing a positive integer amount
        assert account.deposit(100, 1, '2022-01-01') == 100

        # Depositing a positive float amount
        assert account.deposit(100.5, 2, '2022-01-02') == 200.5

        # Depositing a zero amount
        assert account.deposit(0, 3, '2022-01-03') == 200.5

        # Depositing a negative amount should raise ValueError
        with pytest.raises(ValueError):
            account.deposit(-100, 4, '2022-01-04')

        # Depositing a non-numeric amount should raise ValueError
        with pytest.raises(ValueError):
            account.deposit('abc', 5, '2022-01-05')

    # Test for withdraw method
    def test_withdraw(self):
        account = Account(123456, 200)

        # Withdrawing an amount less than the balance
        assert account.withdraw(100, 1, '2022-01-01') == 100

        # Withdrawing an amount equal to the balance
        assert account.withdraw(100, 2, '2022-01-02') == 0

        # Withdrawing an amount greater than the balance should raise ValueError
        with pytest.raises(ValueError):
            account.withdraw(100, 3, '2022-01-03')

        # Withdrawing a zero amount
        assert account.withdraw(0, 4, '2022-01-04') == 0

        # Withdrawing a negative amount should raise ValueError
        with pytest.raises(ValueError):
            account.withdraw(-100, 5, '2022-01-05')

        # Withdrawing a non-numeric amount should raise ValueError
        with pytest.raises(ValueError):
            account.withdraw('abc', 6, '2022-01-06')

    # Test for get_account_statement method
    def test_get_account_statement(self):
        account = Account(123456)

        # Getting the account statement when there are no transactions
        assert account.get_account_statement() == []

        # Getting the account statement when there is one transaction
        account.deposit(100, 1, '2022-01-01')
        assert account.get_account_statement() == [{'transaction_id': 1, 'type': 'deposit', 'amount': 100, 'timestamp': '2022-01-01'}]

        # Getting the account statement when there are multiple transactions
        account.withdraw(50, 2, '2022-01-02')
        assert account.get_account_statement() == [{'transaction_id': 1, 'type': 'deposit', 'amount': 100, 'timestamp': '2022-01-01'},
                                                   {'transaction_id': 2, 'type': 'withdraw', 'amount': 50, 'timestamp': '2022-01-02'}]