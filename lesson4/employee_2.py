"""
Для класса Employee и Client, опишите магический метод сложения таким образом, чтобы результатом сложения
было число, а прибавлять можно было только числа или другие объекты дочерних классов Employee

"""


class Employee:
    def __init__(self, pay):
        self.pay = pay

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        elif str(other).isnumeric():
            return self.pay + other
        else:
            raise TypeError('прибавлять можно было только числа или другие объекты дочерних классов Employee')

class Client:

    def __init__(self, pay):
        self.pay = pay

    def __add__(self, other):
        if isinstance(other, Employee):
            return other.pay
        elif str(other).isnumeric():
            return other
        else:
            raise TypeError('прибавлять можно было только числа или другие объекты дочерних классов Employee')


class Developer(Employee):
    def __init__(self, pay):
        super().__init__(pay)


class Manager(Employee):
    def __init__(self, pay):
        super().__init__(pay)


# код для проверки
users = [Employee(50000), Client(100000), Developer(50000), Manager(50000)]

total_salary = 0
for user in users:
    total_salary = user + total_salary

print(total_salary)
# Вывод: 150000
