"""
Напишите класс Person, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя и возраст человека
- display(self): метод, выводящий на экран имя и возраст человека
- from_birth_year(cls, name, birth_year): класс-метод, принимающий имя и год рождения человека и
возвращающий объект класса Person;
- is_adult(cls, age): статический метод, принимающий возраст человека и возвращающий True,
если он старше 18 лет, и False в противном случае
"""
from datetime import datetime
from typing import Self


class Person:
    """Класс человека"""
    name: str
    age: int


    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


    def display(self) -> None:
        print(f"{self.name} is {self.age} years old")


    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> Self:
        age = datetime.now().year - birth_year - 4
        return cls(name, age)


    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

# код для проверки 
person1 = Person("John", 28)
person1.display()  # John is 28 years old

person2 = Person.from_birth_year("Mike", 1995)
person2.display()  # Mike is 26 years old

print(Person.is_adult(20))  # True
print(Person.is_adult(15))  # False
