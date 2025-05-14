from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance
        
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def balance(self):
        return self._balance
    
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display_account_type():
        pass


class CurrentAccount(BankAccount):
    limit = -5000

    def deposit(self, amount):
        self._balance += amount
        print(f"DEPOSITED: {amount}! CURRENT BALANCE: {self.balance}! ACC NO. {self.account_number}")

    def withdraw(self, amount):
        if self._balance - amount >= self.limit:
            self._balance -= amount
            print(f"WITHDRAWING: {amount}! CURRENT BALANCE: {self.balance}! ACC NO. {self.account_number}")
        else:
            print("UNABLE TO WITHDRAW")
    
    def display_account_type(self):
        return "Current Account"
    
class SavingAccount(BankAccount):
    def deposit(self, amount):
        self._balance += amount
        print(f"DEPOSITED: {amount}! CURRENT BALANCE: {self.balance}! ACC NO. {self.account_number}")
    
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"WITHDRAWING: {amount}! CURRENT BALANCE: {self.balance}! ACC NO. {self.account_number}")
        else:
            print("UNABLE TO WITHDRAW")
    
    def display_account_type(self):
        return "Savings Account"

def print_account_details(account):
    print("----------------------------------------------------------------")
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance}")
    print(f"Type: {account.display_account_type()}")
    print("----------------------------------------------------------------")

save1 = SavingAccount("SA123", 1200)
save2 = SavingAccount("SA321", 15000)
save2.deposit(1000)
save2.withdraw(200)

current1 = CurrentAccount("CA456", -200)
current2 = CurrentAccount("CA654", 500)
current2.withdraw(800)
current2.deposit(200)

accounts = [save1, save2, current1, current2]
for acc in accounts:
    print_account_details(acc)
    
