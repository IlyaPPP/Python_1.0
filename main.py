""" Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза
больше журавликов, чем Петя и Сережа вместе?
Пример:

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10 """

x = int(input("Введите число журавликов: "))
print("Катя сделала: ", x // 3 * 2)
print("Петя сделал: ", x // 6)
print("Сережа сделал: ", x // 6)
