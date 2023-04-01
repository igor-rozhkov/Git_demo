# x = 5
# if x > 5:
#     print('yes')
# else:
#     print('no')

# num1 = int(input())
# num2 = int(input())
# operator = input()
# if num2 == 0 and operator == '/':
#     try:
#         result = num1 / num2
#         print(f'xnj {result}')
#     except ZeroDivisionError:
#         print('no delenie')
#
# # print(num1 / num2)

# num = 0
# while num < 5:
#     print(num)
#     num +=1

# message = 'Hello'
# i = 1
# while i < 6:
#     print(i, message)
#     if i == 3:
#         break
#     i += 1

# message = 'Hello'
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i, message)
# i = 10
# for i in range(6):
#     print(i)
# print(i)

# for i in range(1, 6, 2):
#     print(i)

# for i in 'Hello':
#     print(i)
# print(-150%3)

# Дз по второму уроку
# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

# health = int(input())
# if health <= 0:
#     print(False)
# else:
#     print(True)

#
# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным. Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
# x = int(input())
# if x % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')
#
# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года, которые делятся
# без остатка на 4 (2004, 2008) и не являются столетиями (500, 600). Однако, если год делится без остатка  на 400,
# он также считается високосным (1200, 2000)
# x = int(input())
# if x % 400 == 0 or x % 4 == 0 and x % 100 != 0:
#     print('Високосный')
# else:
#     print('Невисокосный')
#
# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно. Текст и количество повторений нужно ввести с помощью input()
# x = input('Введите текст: ')
# y = int(input('Сколько раз повторить? Введите число: '))
# i = 0
# while i < y:
#     print(x)
#     i += 1
#
# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}
# num1 = int(input('Первое число: '))
# num2 = int(input('Второе число: '))
# operator = input('Введите оператор: ')
# if operator == '/':
#     if num2 != 0:
#         result = num1 / num2
#         print(f'Результат : {num1} {operator} {num2} = {result}')
#     else:
#         print('Нельзя делить на ноль!')
# elif operator == '+':
#     result = num1 + num2
#     print(f'Результат : {num1} {operator} {num2} = {result}')
# elif operator == '-':
#     result = num1 - num2
#     print(f'Результат : {num1} {operator} {num2} = {result}')
# elif operator == '*':
#     result = num1 * num2
#     print(f'Результат : {num1} {operator} {num2} = {result}')
# else:
#     print('Введен неверный оператор!')





