class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
        
    def withdraw(self, amount):
        self._balance -= amount
        
def main():
    account = Account(100)
    account.deposit(52)
    account.withdraw(51)
    print(account.balance)
    
if __name__ == "__main__":
    main()