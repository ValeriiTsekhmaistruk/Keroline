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
        search_query = ' '.join(text)
        url = 'https://google.com/search?q=' + search_query
        print('вот что есть:')
        webbrowser.get().open(url)

    @staticmethod
    def say_time(text):  # время
        time_word = ('время', 'времени', 'час', 'часов')
        date_word = ('дата', 'число', 'дату')

        if bool(set(time_word) & set(text)):
            print(time.strftime('%H:%M', time.localtime()))
        elif bool(set(date_word) & set(text)):
            print(time.strftime('%m.%d.%Y', time.localtime()))
        elif 'день' in text:
            print(time.strftime('%A', time.localtime()))

    @staticmethod
    def get_weather(text):  # погода
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
        multi_word = ('умнож', 'умножить', '*')
        div_word = ('подели', 'раздели', '/')
        sum_word = ('плюс', '+')
        sub_word = ('минус', '-')
        num = list(map(int, filter(lambda x: x.isdigit(), text)))

        if bool(set(multi_word) & set(text)):
            print(num[0] * num[1])
        elif bool(set(div_word) & set(text)):
            if num[1] == 0:
                print('Делить на 0 нельзя!!!')
            else:
                print(num[0] / num[1])
        elif bool(set(sum_word) & set(text)):
            print(num[0] + num[1])
        elif bool(set(sub_word) & set(text)):
            print(num[0] - num[1])

    @staticmethod
    def math_sqrt(text):  # математический корень
        num = list(map(int, filter(lambda x: x.isdigit(), text)))
        print(math.sqrt(num[0]))

    @staticmethod
    def math_exp(text):
        num = list(map(int, filter(lambda x: x.isdigit(), text)))
        if 'квадрат' in text:
            print(num[0]**2)
        elif 'куб' in text:
            print(num[0]**3)
        else:
            print(num[0]**num[1])


commands = {
    ('привет', 'пока', 'спасибо', 'дела'): Commands.communication,
    ('найди', 'поищи'): Commands.search_google,
    ('время', 'времени', 'час', 'часов', 'дата', 'число', 'дату', 'день'): Commands.say_time,
    ('погода', 'погоду', 'погоды'): Commands.get_weather,
    ('+', '-', '*', '/', 'плюс', 'минус', 'умнож', 'умножить', 'подели', 'раздели'): Mathematics.simple_math,
    'корень': Mathematics.math_sqrt,
    ('степень', 'степени', 'квадрат', 'куб'): Mathematics.math_exp
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
