class BankAccount:
    def _init_(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @property
    def account_number(self):
        return self.account_number
    
    @property
    def balance(self):
        return self.balance
    
    def deposit(amount):
        pass

    def withdraw(ammount):
        pass

    def display_account_type():
        pass

class CurrentAccount(BankAccount):
    Overdraft_limit = -5000
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.Overdraft_limit:
            self.balance -= amount

    def display_account_type():
        return "Current Account"
    
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


    def display_account_type():
        return "Savings Account"

def print_account_details(account):
    print("Account Number: ", account.account_number)
    print("Balance: ", account.balance)
    print("Type: ", account.account_type)

if __name__ == "__main__":
    sa1 = SavingsAccount()
  

    sa1.account_number("WOW")
    sa1.balance(10000)
    sa1.deposit(100)
    sa1.withdraw(300)
    sa1.display_account_type

    print_account_details(sa1)
    