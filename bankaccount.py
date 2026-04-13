class BankAccount:
    def __init__(self, acc_num, holder, initial_balance, overdraft_limit=0):
        self.__account_number = acc_num
        self.__account_holder = holder
        self.__balance = initial_balance
        self.__transactions = []
        self.__overdraft_limit = overdraft_limit

    
    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @property
    def overdraft_limit(self):
        return self.__overdraft_limit

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("No negative deposits")
        self.__balance += amount
        self.__transactions.append(f"Deposit {amount}")

    def withdraw(self, amount):
        if amount > self.__balance + self.__overdraft_limit:
            raise ValueError("Exceeds overdraft limit")
        self.__balance -= amount
        self.__transactions.append(f"Withdraw {amount}")

    def display_account_info(self):
        print(f"Account {self.__account_number} – {self.__account_holder}")
        print(f"Balance: {self.__balance}")
        print(f"Overdraft limit: {self.__overdraft_limit}")

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
   
    acc = BankAccount("001", "Maria", 1000, overdraft_limit=500)
    acc.withdraw(1200)  
    acc.display_account_info()
    acc.show_history()

    print("-----")

    s = SavingsAccount("002", "Alex", 1000, 0.05)
    s.apply_interest()
    s.display_account_info()
