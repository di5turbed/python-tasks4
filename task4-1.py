from math import factorial

kvadrat = [x ** 2 for x in range(1, 11)]
print(kvadrat)

day = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
day_numbers = {day: num + 1 for num, day in enumerate(day)}
print(day_numbers)

biblioteks = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
tags = {biblio.lower() for biblio in biblioteks}
print(tags)

numbers = [1, 3, 4, 87, 98, 15, 7, 4]
chetnie = [x for x in numbers if x % 2 == 0]
print(chetnie)


def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

factorials = {n: fact(n) for n in range(1, 6)}
print(factorials)

# Через библиотеку, которую импортировал вначале программы
factorials = {n: factorial(n) for n in range(1, 6)}
print(factorials)
