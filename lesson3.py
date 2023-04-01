# from typing import List

# # Получаем кортеж из списка
# numbers = [1, 2, 3, 4, 5]
# new_l = tuple([x * x for x in numbers if x % 2])
# print(new_l)

# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# a = my_list[2]
# print(*a)

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# digi = [i for i in list_1 if type(i) is int]
# print(sum(digi))
# stroki = [i for i in list_1 if type(i) is str and 'a' in i]
# print(*stroki)

# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
#
a = ['cat', 'dog', 'horse', 'cow']
b = tuple(a)
print(b)
# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family_1 = input()
# family_2 = input()
# c_1 = len(family_1.split(', '))
# c_2 = len(family_2.split(', '))
# print('Equal' if c_1 == c_2 else family_1 if c_1 > c_2 else family_2)

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

# film = {
#     'title': '8 миля',
#     'director': 'Кёртис Хэнсон',
#     'year': 2002, 'budget': 41_000_000,
#     'main_actor': 'Эминем',
#     'slogan': 'Каждый миг - это шанс!'
# }
# print(film.keys())
# print(film.values())
# print(film.items())

# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
#
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
#
# list = [1, 2, 3, 4, 5, 3, 2, 1]
# l_new = []
# for i in list:
#     if i not in l_new:
#         l_new.append(i)
# print(l_new)
#
# list_1 = [1, 2, 3, 4, 5, 3, 2, 1]
# new_list = list(set(list_1)) #преобразуем в множество и дубликаты удаляются
# print(new_list)

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
# print(set1.intersection(set2))
#      - найдите значения, которые не встречаются в обоих множествах
# print(result)
# print(set2.symmetric_difference(set1))
#      - проверьте являются ли эти множества подмножествами друг друга
# print(set1 in set2)
