class BankAccount:
    def __init__(self):
        self._balance = 0


    @property
    def balance(self):
        return self._balance
    
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative")
        self._balance += amount
        print(f'Deposited: {amount}. New balance: {self._balance}')

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount must be non-negative")
        if amount >= self._balance:
            raise ValueError("Insufficient funds for withdrawal")
        self._balance -= amount
        print(f'Withdrew: {amount}. New balance: {self._balance}')


# owner_1 = BankAccount()
# owner_1.deposit(1000)
# owner_1.withdraw(500)
# print(f'Final balance: {owner_1.balance}')  # Final balance: 500

# Main program without error handling
owner_1 = BankAccount()

deposit_amount = float(input("Enter amount to deposit: "))
owner_1.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
owner_1.withdraw(withdraw_amount)

print(f'Final balance: {owner_1.balance}')