import sys


def communication(text): # общение
    hello = ('привет')
    goodbye = ('пока')
    thanks = ('спасибо')
    how_are_you = ('дела')

    for word in text:
        if word in hello:
            print('привет')
        elif word in goodbye:
            print('пока')
            sys.exit()
        elif word in thanks:
            print('пожалуйста')
        elif word in how_are_you:
            print('отлично')


def math(text): # математика
    for word in text:
        if word in black_list:
            text.remove(word)

    num = []
    multi = ('умнож', 'умножить', '*')
    division = ('подели', 'раздели', '/')
    summ = ('плюс', '+')
    sub = ('минус', '-')

    for word in text:
        if word.isdigit():
            num.append(int(word))
    text.remove(str(num[0]))
    text.remove(str(num[1]))

    if text[0] in multi:
        res = num[0] * num[1]
        print(res)
    elif text[0] in division:
        res = num[0] / num[1]
        print(res)
    elif text[0] in summ:
        res = num[0] + num[1]
        print(res)
    elif text[0] in sub:
        res = num[0] - num[1]
        print(res)


commands = {
    ('привет', 'пока', 'спасибо', 'дела'): communication,
    ('+', '-', '*', '/', 'плюс', 'минус', 'умнож', 'умножить', 'подели', 'раздели'): math
}

black_list = ('на', 'пожалуйста')


def search_command(command):  # поиск по списку команд
    text = command.lower()
    text = text.split(" ")

    for key in commands.keys():
        for word in text:
            if word in key:
                commands[key](text)
                break


print('Привет! Я Керолайн, твой персональний голосовой асистент. Спрашивай! ')

while True:
    user_command = input()
    search_command(user_command)