import uuid
from datetime import datetime
from account import Account

class Transaction:
    def __init__(self, account: Account):
        self.account = account

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        transaction_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        try:
            new_balance = self.account.deposit(amount, transaction_id, timestamp)
            return {
                "status": "success",
                "transaction_id": transaction_id,
                "new_balance": new_balance
            }
        except ValueError as e:
            return {
                "status": "failed",
                "error": str(e)
            }

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        transaction_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        try:
            new_balance = self.account.withdraw(amount, transaction_id, timestamp)
            return {
                "status": "success",
                "transaction_id": transaction_id,
                "new_balance": new_balance
            }
        except ValueError as e:
            return {
                "status": "failed",
                "error": str(e)
            }
