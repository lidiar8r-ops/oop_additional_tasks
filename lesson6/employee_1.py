"""
Напишите класс Person, представляющий человека, имеющий следующие атрибуты:

- имя
- возраст
- зарплата

Напишите класс Employee, у которого конструктор проверяет, что возраст не меньше 18 и не больше 127 лет.
В случае, если возраст не укладывается в заданные рамки, вызвать исключение ValueError и прервать выполнение программы.
Также в конструкторе необходимо проверять уровень зарплаты, который должен быть не меньше 16242. Вызывать ValueError
исключение.

Вызванные исключения должны пояснять в чем именно произошла ошибка.
"""


class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        if age < 18 or age > 127:
            raise ValueError('Возраст должен быть не меньше 18 и не больше 127')
        else:
            self.age = age

        if pay < 16242:
            raise ValueError('Оплата труда не может быть меньше 16242')
        else:
            self.pay = pay




class Person(Employee):
    def __init__(self, name, age, pay):
        super().__init__(name, age, pay)




# код для проверки
try:
    employee = Employee('John', 30, 5000)
    # raises ValueError('Оплата труда не может быть меньше 16242')
except ValueError as e:
    print(e)

try:
    employee = Employee("Jane", 17, 50000)
# raises ValueError('Возраст должен быть не меньше 18 и не больше 127')

except ValueError as e:
    print(e)

try:
    employee = Employee("Kate", 175, 50000)
# raises ValueError('Возраст должен быть не меньше 18 и не больше 127')

except ValueError as e:
    print(e)
