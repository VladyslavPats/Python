class User:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__accounts = []

    def add_account(self, account):
        self.__accounts.append(account)

    def get_accounts(self):
        return self.__accounts

    def get_full_name(self):
        return f"{self.__name} {self.__surname}"


class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.__account_number = account_number
        self.__balance = balance
        self.__owner = owner

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    def get_account_number(self):
        return self.__account_number


class BankSystem:
    def __init__(self):
        self.__account_counter = 1000

    def create_user(self, name, surname, age):
        return User(name, surname, age)

    def create_account(self, user, initial_balance):
        account = BankAccount(self.__account_counter, user, initial_balance)
        user.add_account(account)
        self.__account_counter += 1
        return account

    def deposit(self, account, amount):
        account.deposit(amount)

    def withdraw(self, account, amount):
        account.withdraw(amount)

    def transfer(self, sender_account, receiver_account, amount):
        if sender_account.get_balance() >= amount:
            sender_account.withdraw(amount)
            receiver_account.deposit(amount)

bank_system = BankSystem()
user1 = bank_system.create_user("John", "Doe", 35)
account1 = bank_system.create_account(user1, 1000)
bank_system.deposit(account1, 500)
bank_system.withdraw(account1, 200)

user2 = bank_system.create_user("Alice", "Smith", 28)
account2 = bank_system.create_account(user2, 1500)
bank_system.transfer(account1, account2, 300)

print(account1.get_balance())
print(account2.get_balance())
