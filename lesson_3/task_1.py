""" task 1 and 2 """

my_dickt = {

    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четире",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
}


def num_translate(num_word):
    return my_dickt.get(num_word)


def num_translate_adv(num_word):
    to_key = my_dickt.get(num_word.lower())

    if to_key:
        return to_key.capitalize() if num_word[0].isupper() else to_key

    return None 
print(num_translate("zero"))