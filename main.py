import sys
import webbrowser
#from pyowm import OWM


class Commands:

    def __init__(self):
        pass

    @staticmethod
    def communication(text):  # общение
        hello = 'привет'
        goodbye = 'пока'
        thanks = 'спасибо'
        how_are_you = 'дела'

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

    @staticmethod
    def math(text):  # математика
        black_list = ('на', 'пожалуйста', 'сколько', 'будет')
        for word in text:
            if word in black_list:
                text.remove(word)

        num = []
        multi = ('умнож', 'умножить', '*')
        division = ('подели', 'раздели', '/')
        summ = ('плюс', '+')
        sub = ('минус', '-')

        try:
            for word in text:
                if word.isdigit():
                    num.append(int(word))
            text.remove(str(num[0]))
            text.remove(str(num[1]))
        except IndexError:
            print('Ошибка в данних')
            return
        if text[0] in multi:
            res = num[0] * num[1]
            print(res)
        elif text[0] in division:
            res = 0
            try:
                res = num[0] / num[1]
            except ZeroDivisionError:
                print('Нельзя делить на 0!')
            else:
                print(res)
        elif text[0] in summ:
            res = num[0] + num[1]
            print(res)
        elif text[0] in sub:
            res = num[0] - num[1]
            print(res)

    @staticmethod
    def search_google(text):  # поиск в google
        text.pop(0)
        search_trem = ' '.join(text)
        url = 'https://google.com/search?q=' + search_trem
        print('вот что есть:')
        webbrowser.get().open(url)

    #@staticmethod
    #def get_weather(text):
    #    black_list = ('погода', 'в')
    #    for word in text:
    #        print(text)
    #        if word in black_list:
    #            text.remove(word)
    #    print(text)


commands = {
    ('привет', 'пока', 'спасибо', 'дела'): Commands.communication,
    ('+', '-', '*', '/', 'плюс', 'минус', 'умнож', 'умножить', 'подели', 'раздели'): Commands.math,
    ('найди', 'поищи'): Commands.search_google,
    #('погода'): Commands.get_weather
    }


def search_command(command):  # поиск по списку команд
    text = command.lower()
    text = text.split(" ")

    for key in commands.keys():
        for word in text:
            if word in key:
                commands[key](text)
                break


if __name__ == '__main__':
    print('Привет! Я Керолайн, твой персональний голосовой асистент. Спрашивай! ')
    while True:
        user_command = input()
        search_command(user_command)
