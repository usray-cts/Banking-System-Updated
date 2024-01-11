from account import Account
from transaction import Transaction
from bank import Bank

bank = Bank()
account = bank.create_account("12345678")
if isinstance(account, Account):
    transaction = Transaction(account)
    print(transaction.deposit(500))
    print(transaction.withdraw(200))
    try:
        print(transaction.withdraw(400))
    except ValueError as e:
        print("Error: ", str(e))
    print(account.get_account_statement())

