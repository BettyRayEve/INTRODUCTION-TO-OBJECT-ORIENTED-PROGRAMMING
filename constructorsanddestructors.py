class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []
        print(f"Opened {owner}'s account with {balance}")

    def deposit(self, amt):
        if amt > 0:
            self.balance += amt
            self.history.append(f"Deposit {amt}")
            print("Deposited", amt)
        else:
            print("Deposit must be positive")

    def withdraw(self, amt):
        if amt <= 0:
            print("Withdraw must be positive")
        elif amt <= self.balance:
            self.balance -= amt
            self.history.append(f"Withdraw {amt}")
            print("Withdrew", amt)
        else:
            print("Insufficient funds")

    def interest(self, rate):
        gain = self.balance * rate
        self.balance += gain
        self.history.append(f"Interest {gain}")
        print("Interest added", gain)

    def statement(self):
        print("Statement for", self.owner)
        for line in self.history:
            print(" -", line)
        print("Balance:", self.balance)

    def __del__(self):
        print(f"Closed {self.owner}'s account")

acc = BankAccount("Ada", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.interest(0.05)
acc.statement()
del acc