class BankAccount:
    def __init__(self, acc_num, holder, initial_balance):
        self.__account_number = acc_num
        self.__account_holder = holder
        self.__balance = initial_balance
        self.__transactions = []

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("No negative deposits")
        self.__balance += amount
        self.__transactions.append(f"Deposit {amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Withdraw exceeds balance")
        self.__balance -= amount
        self.__transactions.append(f"Withdraw {amount}")

    def display_account_info(self):
        print(f"Account {self.__account_number} – {self.__account_holder}")
        print(f"Balance: {self.__balance}")

    def show_history(self):
        for t in self.__transactions:
            print(t)

class SavingsAccount(BankAccount):
    def __init__(self, acc_num, holder, initial_balance, rate):
        super().__init__(acc_num, holder, initial_balance)
        self.rate = rate

    def apply_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)


if __name__ == "__main__":
    acc = BankAccount("001", "Maria", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    acc.display_account_info()
    acc.show_history()

    s = SavingsAccount("002", "Alex", 1000, 0.05)
    s.apply_interest()
    s.display_account_info()