"""3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов», задаем число
 2 — получаем «2 процента». Вывести все склонения для проверки.
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное ДЗ."""

a = "Процент"
b = "Процента"
c = "Процентов"
i = int(input("Введите количество процентов:"))
numbs = {11,12,13,14}
for z in range(i ,20):
        if i in numbs:
            print(i, c.lower())
            break
        elif i % 10 == 1:
            print(i, a.lower())
            break
        elif i % 10 > 1 and i % 10 <5:
            print(i, b.lower())
            break
        else:
            print(i, c.lower())
            break
   
""" my_dictionary={

        "1":"процент",
        "2":"процента",
        "3":"процента",
        "4":"процента",
        "5":"процентов",
        "6":"процентов",
        "7":"процентов",
        "8":"процентов",
        "9":"процентов",
        "10":"процентов",
        "11":"процентов",
        "12":"процентов",
        "13":"процентов",
        "14":"процентов",
        "15":"процентов",
        "16":"процентов",
        "17":"процентов",
        "18":"процентов",
        "19":"процентов",
        "20":"процентов"
    }"""
        