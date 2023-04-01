# def calc(a, b=2):
#     return a * b
#
#
# print(calc(10, b=3))

# def person(age, f_name, l_name):
#     return f'Hello my name is {f_name} {l_name}. I am {age} years old.'
#
#
# print(person(25, 'Anna', 'Grand'))

# def pattern(length, char1, char2):
#     return (char1 + char2) * length + char1
#
#
# print(pattern(8, "(-_-)", '*'))

# mult = lambda x, y: x * y
# print(mult(5, 6))

# l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5, 19, 21]
# filtered = list(filter(lambda x: isinstance(x, int) and not x % 2, l))
# print(filtered)
#
# l1 = [100, 20, 30, 50]
# power = list(map(lambda x: x ** 2 if isinstance(x, int) else l, l))
# print(power)

# def my_decorator(func):
#     def wrapper(arg):
#         print('Я - обертка')
#         func(arg)
#         print('Закончили заворачивать')
#
#     return wrapper
#
# @my_decorator
# def say_hello(name):
#     print(f'Hello, {name}')
#
# say_hello('Ivan')
# # say_hello = sy_decorator(say_hello)

# def milk(func):
#     def wrapper():
#         print('hot milk')
#         func()
#     return wrapper
#
# def sugar(func):
#     def wrapper():
#         print('sugar')
#         func()
#     return wrapper
# @sugar
# def coffee():
#     print('coffee')
# coffee()

# import datetime

# import datetime as datetime
#
# current_time = datetime.date.today()
# bday = 1990
# print(f'Age = {current_time.year - bday}')

# import lesson4_module as l4m
# print(l4m.hello('Stas'))
#
# from lesson4_module import sum as s
# print(s(5, 29))

# from lesson4_module * # вызвать все функции

# import time
# print(time.perf_counter())

# def func(**kwargs) #прими произвольное количество именованных аргументов.

# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
# def square(a):
#     return a * 4, a ** 2, 2*a ** 0.5
#
#
# print(tuple(square(int(input()))))
#
# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
# def func(**kwargs):
#     for a, b in kwargs.items():
#         print(f'{a}: {b}')
#
# print(func(name='John', last_name='Smith', age=35, position='web developer'))
#
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# new_list = list(filter(lambda x: x > 0, my_list))
# print(new_list)


# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# my_list = [20, -3, 15, 2, -1, -21]
# new_list = list(map(lambda x: x*x, my_list))
# print(new_list)

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
import time


def timer(func):
    def wrapper():
        print(f'Время запуска:{time.localtime()}')
        func()
        print(f'Время выполнения функции:{time.perf_counter()}')
    return wrapper


@timer
def suma(a, b):
    return a + b
print(suma(50, 100))


# def my_decorator(func):
#     def wrapper(arg):
#         print('Я - обертка')
#         func(arg)
#         print('Закончили заворачивать')
#
#     return wrapper
#
#
# @my_decorator
# def say_hello(name):
#     print(f'Вызов основной функции: Hello, {name}')
#
#
# say_hello('Ivan')

# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
