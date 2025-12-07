"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""
from datetime import date


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        current_year = date.today().year
        if year <= current_year:
            self.year = year
        else:
            raise ValueError("Эта машина еще не была выпущена")



# код для проверки
car = Car('Toyota', 'Corolla', 2022)

try:
    car = Car('Toyota', 'Corolla', 3000)
except ValueError as e:
    print(f"Ошибка: {e}")# raises Exception('Эта машина еще не была выпущена')
