"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, которое возвращает текущий баланс счета
- deposit(self, amount): метод, который позволяет внести деньги на счет
- withdraw(self, amount): метод, который позволяет снять деньги со счета
- close(self): метод, который закрывает счет и возвращает оставшиеся на нем деньги

Для свойства balance используйте декоратор @property.
"""


class BankAccount:
    _balance: float


    def __init__(self, balance: float) -> None:
        self._balance = balance


    @property
    def balance(self) -> float:
        return self._balance


    def deposit(self, amount: float) -> None:
        self._balance += amount


    def withdraw(self, amount: float) -> None:
        self._balance -= amount


    def close(self) -> float:
        amount = self._balance
        self._balance = 0
        return amount


# код для проверки 
account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500

account.withdraw(200)
print(account.balance)  # 1300

account.close()
print(account.balance)  # 0
