from typing import List


class Account:

    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions: List[int] = []

    def handle_transaction(self, transaction_amount: int):
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")

        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        return self.handle_transaction(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        return iter(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __getitem__(self, index):
        return self._transactions[index]

    def __gt__(self, other):
        return self.amount > other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __add__(self, other):
        new_account = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        new_account._transactions = self._transactions + other._transactions

        return new_account

# examples
acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)