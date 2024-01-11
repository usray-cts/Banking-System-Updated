class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount, transaction_id, timestamp):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Deposit amount must be positive and a number.")
        self.balance += amount
        self.transactions.append({
            'transaction_id': transaction_id,
            'type': 'deposit',
            'amount': amount,
            'timestamp': timestamp
        })
        return self.balance

    def withdraw(self, amount, transaction_id, timestamp):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Withdrawal amount must be positive and a number.")
        elif amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        self.transactions.append({
            'transaction_id': transaction_id,
            'type': 'withdraw',
            'amount': amount,
            'timestamp': timestamp
        })
        return self.balance

    def get_account_statement(self):
        if not self.transactions:
            return []
        return self.transactions
