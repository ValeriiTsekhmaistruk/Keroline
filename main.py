import sys
import webbrowser
import math
import time


class Assistant:
    name = 'Керолайн'
    city = 'Николаев'


class Commands:

    def __init__(self):
        pass

    @staticmethod
    def communication(text):  # общение

        for word in text:
            if word in 'привет':
                print('привет')
            elif word in 'пока':
                print('пока')
                sys.exit()
            elif word in 'спасибо':
                print('пожалуйста')
            elif word in 'дела':
                print('отлично')

    @staticmethod
    def search_google(text):  # поиск в google
        text.pop(0)
        search_trem = ' '.join(text)
        url = 'https://google.com/search?q=' + search_trem
        print('вот что есть:')
        webbrowser.get().open(url)

    @staticmethod
    def say_time(text):
        black_list = ('скажи', 'пожалуйста', 'который', 'какой',
                      'сейчас', 'какое', 'который', 'сколько',
                      'сегодня', 'который', 'назови', 'недели')
        clear_text = list(filter(lambda item: item not in black_list, text))

        if clear_text[0] in ('время', 'времени', 'час', 'часов'):
            print(time.strftime('%H:%M', time.localtime()))
        elif clear_text[0] in ('дата', 'число', 'дату'):
            print(time.strftime('%m.%d.%Y', time.localtime()))
        elif clear_text[0] in ('день'):
            print(time.strftime('%A', time.localtime()))

    @staticmethod
    def get_weather(text):
        black_list = ('покажи', 'прогноз', 'в', 'погода', 'погоду', 'погоды')
        clear_text = list(filter(lambda item: item not in black_list, text))

        if len(clear_text) == 0:
            url = 'https://google.com/search?q=' + f'погода  в {Assistant.city}'
            webbrowser.get().open(url)
        else:
            url = 'https://google.com/search?q=' + f'погода  в {clear_text[0]}'
            webbrowser.get().open(url)


class Mathematics:

    def __init__(self):
        pass

    @staticmethod
    def simple_math(text):  # математика
        black_list = ('на', 'пожалуйста', 'сколько', 'будет')
        clear_text = list(filter(lambda item: item not in black_list, text))
        num = []

        try:
            for word in clear_text:
                if word.isdigit():
                    num.append(int(word))
            clear_text.remove(str(num[0]))
            clear_text.remove(str(num[1]))
        except IndexError:
            print('Ошибка в данних')
            return
        if clear_text[0] in ('умнож', 'умножить', '*'):
            res = num[0] * num[1]
            print(res)
        elif clear_text[0] in ('подели', 'раздели', '/'):
            res = 0
            try:
                res = num[0] / num[1]
            except ZeroDivisionError:
                print('Нельзя делить на 0!')
            else:
                print(res)
        elif clear_text[0] in ('плюс', '+'):
            res = num[0] + num[1]
            print(res)
        elif clear_text[0] in ('минус', '-'):
            res = num[0] - num[1]
            print(res)

    @staticmethod
    def math_sqrt(text):
        num = list(filter(lambda x: x.isdigit(), text))
        print(math.sqrt(int(num[0])))


commands = {
    ('привет', 'пока', 'спасибо', 'дела'): Commands.communication,
    ('найди', 'поищи'): Commands.search_google,
    ('время', 'времени', 'час', 'часов', 'дата', 'число', 'дату', 'день'): Commands.say_time,
    ('погода', 'погоду', 'погоды'): Commands.get_weather,
    ('+', '-', '*', '/', 'плюс', 'минус', 'умнож', 'умножить', 'подели', 'раздели'): Mathematics.simple_math,
    'корень': Mathematics.math_sqrt,
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
