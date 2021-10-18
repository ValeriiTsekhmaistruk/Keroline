import sys
import webbrowser
import math
import time
import pyttsx3


class Assistant:
    name = 'Керолайн'
    city = 'Николаев'
    voice = False


class Voice:

    def __init__(self):
        pass

    @staticmethod
    def say(string):
        match Assistant.voice:
            case True:
                engine = pyttsx3.init()
                engine.say(string)
                engine.runAndWait()
            case _:
                return


class Commands:

    def __init__(self):
        pass

    @staticmethod
    def communication(text):  # общение
        hi_words = ('привет', 'приветствую')
        bye_words = ('пока', 'прощай')
        ths_words = ('спасибо', 'благодарю')
        info_words = ('кто', 'ты')
        command_words = ('делаешь', 'умеешь', 'можешь')

        if bool(set(hi_words) & set(text)):
            print('привет')
            Voice.say('привет')
        elif bool(set(bye_words) & set(text)):
            print('пока')
            Voice.say('пока')
            sys.exit()
        elif bool(set(ths_words) & set(text)):
            print('пожалуйста')
            Voice.say('пожалуйста')
        elif bool(set(info_words) & set(text)):
            print('Я Керолайн, ваш личный голосовой ассистент')
            Voice.say('Я Керолайн, ваш личный голосовой ассистент')
        elif bool(set(command_words) & set(text)):
            print('Затрудняюсь ответить, меня постоянно улучшают')
            Voice.say('Затрудняюсь ответить, меня постоянно улучшают')

    @staticmethod
    def search_google(text):  # поиск в google
        text.pop(0)
        search_query = ' '.join(text)
        url = 'https://google.com/search?q=' + search_query
        print('вот что есть:')
        Voice.say('вот что есть:')
        webbrowser.get().open(url)

    @staticmethod
    def say_time(text):  # время
        time_word = ('время', 'времени', 'час', 'часов')
        date_word = ('дата', 'число', 'дату')

        if bool(set(time_word) & set(text)):
            print(time.strftime('%H:%M', time.localtime()))
            Voice.say(time.strftime('%H:%M', time.localtime()))
        elif bool(set(date_word) & set(text)):
            print(time.strftime('%m.%d.%Y', time.localtime()))
            Voice.say(time.strftime('%m.%d.%Y', time.localtime()))
        elif 'день' in text:
            print(time.strftime('%A', time.localtime()))
            Voice.say(time.strftime('%A', time.localtime()))

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
        result = None

        if bool(set(multi_word) & set(text)):
            result = (num[0] * num[1])
        elif bool(set(div_word) & set(text)):
            if num[1] == 0:
                result = 'Делить на 0 нельзя!!!'
            else:
                result = (num[0] / num[1])
        elif bool(set(sum_word) & set(text)):
            result = (num[0] + num[1])
        elif bool(set(sub_word) & set(text)):
            result = (num[0] - num[1])

        print(result)
        Voice.say(result)

    @staticmethod
    def math_sqrt(text):  # математический корень
        num = list(map(int, filter(lambda x: x.isdigit(), text)))
        result = math.sqrt(num[0])
        print(result)
        Voice.say(result)

    @staticmethod
    def math_exp(text):
        num = list(map(int, filter(lambda x: x.isdigit(), text)))
        result = None
        if 'квадрат' in text:
            result = (num[0]**2)
        elif 'куб' in text:
            result = (num[0]**3)
        else:
            result = (num[0]**num[1])

        print(result)
        Voice.say(result)


commands = {
    ('привет', 'приветствую', 'пока', 'прощай', 'спасибо', 'благодарю',
     'делаешь', 'умеешь', 'можешь', 'кто', 'ты'): Commands.communication,
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
    print('Привет! Я Кэролайн, ваш личный голосовой ассистент. Спрашивай! ')
    Voice.say('Привет! Я Кэролайн, ваш личный голосовой ассистент. Спрашивай! ')
    while True:
        user_command = input()
        search_command(user_command)
