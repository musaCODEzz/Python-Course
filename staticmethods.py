class BankAccount:
    MIN_BALANCE = 1000

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance


    def deposit(self, amount):
        if self._is_amount_valid(amount):
            self._balance += amount
            print(f'{self.owner} has Deposited {amount}. New balance: {self._balance}')
        else:
            print(f'Invalid deposit amount: {amount}. Must be greater than 0.')

    def _is_amount_valid(self, amount):
        return amount > 0

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0<= rate <= 5
    
owner_1 = BankAccount('Alice', 5000)
owner_1.deposit(00)
print(BankAccount.is_valid_interest_rate(3))  # True
print(BankAccount.is_valid_interest_rate(6))  # False