from typing import List

class Account:

    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions: List[int] = []

    def add_transaction(self, transaction_amount: int):
        self._transactions.append(transaction_amount)
        self.amount += transaction_amount

    def sum_and_print_transactions(self):
        total = sum(self._transactions)
        print(f"Sum of transactions: {total}")

# Example usage
account = Account("John", 100)
account.add_transaction(30)
account.add_transaction(-10)
account.add_transaction(50)

account.sum_and_print_transactions()