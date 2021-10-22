import os
import sys
import webbrowser
import math
import time
import pyttsx3
from collections import namedtuple


class Assistant:
    name = 'Кэролайн'
    city = 'Николаев'
    voice = False

    spotify = 'C:\\Users\\Alan Miller\\AppData\\Roaming\\Spotify\\Spotify.exe'
    telegram = 'D:\\programm\\Telegram Desktop\\Telegram.exe'
    browser = 'C:\\Users\\Alan Miller\\AppData\\Local\\Programs\\Opera GX\\launcher.exe'
    office = 'D:\\programm\\WPS Office\\ksolaunch.exe'


class Voice:

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

    @staticmethod
    def communication(text):
        hi_words = ('привет', 'приветствую')
        bye_words = ('пока', 'прощай')
        ths_words = ('спасибо', 'благодарю')
        info_words = ('кто', '  ')
        command_words = ('делаешь', 'умеешь', 'можешь', 'ты')

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
            print(f'Я {Assistant.name}, ваш личный голосовой ассистент')
            Voice.say(f'Я {Assistant.name}, ваш личный голосовой ассистент')
        elif bool(set(command_words) & set(text)):
            print('Затрудняюсь ответить, меня постоянно улучшают')
            Voice.say('Затрудняюсь ответить, меня постоянно улучшают')

    @staticmethod
    def search_google(text):
        match len(text):
            case 1:
                print('Что именно вы хотите найти?')
                Voice.say('Что именно вы хотите найти?')
                return
        text.pop(0)
        search_query = ' '.join(text)
        url = 'https://google.com/search?q=' + search_query
        print('вот что есть:')
        Voice.say('вот что есть:')
        webbrowser.get().open(url)

    @staticmethod
    def say_time(text):
        time_word = ('время', 'времени', 'час', 'часов')
        full_date_word = ('дата', 'дату')

        if bool(set(time_word) & set(text)):
            print(time.strftime('%H:%M', time.localtime()))
            Voice.say(time.strftime('%H:%M', time.localtime()))
        elif bool(set(full_date_word) & set(text)):
            print(time.strftime('%m.%d.%Y', time.localtime()))
            Voice.say(time.strftime('%m.%d.%Y', time.localtime()))
        elif 'число' in text:
            print(time.strftime('%m.%d', time.localtime()))
            Voice.say(time.strftime('%m.%d', time.localtime()))
        elif 'день' in text:
            print(time.strftime('%A', time.localtime()))
            Voice.say(time.strftime('%A', time.localtime()))

    @staticmethod
    def get_weather(text):
        black_list = ('покажи', 'прогноз', 'в', 'погода', 'погоду', 'погоды')
        clear_text = list(filter(lambda item: item not in black_list, text))

        if len(clear_text) == 0 and Assistant.city == '':
            print('Укажите город')
            Voice.say('Укажите город')
        elif len(clear_text) == 0:
            print('Выполняю')
            Voice.say('Выполняю')
            url = 'https://google.com/search?q=' + f'погода  в {Assistant.city}'
            webbrowser.get().open(url)
        else:
            print('Выполняю')
            Voice.say('Выполняю')
            url = 'https://google.com/search?q=' + f'погода  в {clear_text[0]}'
            webbrowser.get().open(url)

    @staticmethod
    def run_app(text):
        if len(text) < 2:
            print('Укажите приложение')
            Voice.say('Укажите приложение')
            return

        app_list = ('телеграмм', 'спотифай', 'офис', 'браузер')
        clear_text = list(filter(lambda item: item in app_list, text))

        if len(clear_text) == 0:
            print('Приложение не найденно')
            Voice.say('Приложение не найденно')
            return

        def sey(x):
            match x:
                case 'run':
                    print('Выполняю')
                    Voice.say('Выполняю')
                case 'not':
                    print('Приложение не установленно')
                    Voice.say('Приложение не установленно')
        try:
            match clear_text[0]:
                case 'спотифай':
                    if Assistant.spotify == '':
                        sey('not')
                        return
                    os.startfile(Assistant.spotify)
                    sey('run')

                case 'телеграмм':
                    if Assistant.telegram == '':
                        sey('not')
                        return
                    os.startfile(Assistant.telegram)
                    sey('run')

                case 'офис':
                    if Assistant.office == '':
                        sey('not')
                        return
                    os.startfile(Assistant.office)
                    sey('run')

                case 'браузер':
                    if Assistant.browser == '':
                        sey('not')
                        return
                    os.startfile(Assistant.browser)
                    sey('run')
        except FileNotFoundError:
            print('Указан неверный путь к приложению')
            Voice.say('Указан неверный путь к приложению')


class Mathematics:

    @staticmethod
    def simple_math(text):
        multi_word = ('умнож', 'умножить', '*')
        div_word = ('подели', 'раздели', '/')
        sum_word = ('плюс', '+')
        sub_word = ('минус', '-')
        num = list(map(int, filter(lambda x: x.isdigit(), text)))
        match len(num):
            case 1:
                print('Не хватает аргумента')
                Voice.say('Не хватает аргумента')
                return
            case 0:
                print('Укажите аргументы')
                Voice.say('Укажите аргументы')
                return
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
    def math_sqrt(text):
        try:
            num = list(map(int, filter(lambda x: x.isdigit(), text)))
            result = math.sqrt(num[0])
            print(result)
            Voice.say(result)
        except IndexError:
            print('Укажите аргумент')
            Voice.say('Укажите аргумент')
            return

    @staticmethod
    def math_exp(text):
        try:
            num = list(map(int, filter(lambda x: x.isdigit(), text)))

            if 'квадрат' in text:
                result = (num[0]**2)
            elif 'куб' in text:
                result = (num[0]**3)
            else:
                result = (num[0]**num[1])

            print(result)
            Voice.say(result)
        except IndexError:
            print('Укажите аргумент')
            Voice.say('Укажите аргумент')
            return


class KeyWord:
    key_word = namedtuple('key_word', 'words func')

    communication = key_word(('привет', 'приветствую', 'пока', 'прощай', 'спасибо', 'благодарю', 'делаешь',
                              'умеешь', 'можешь', 'кто', 'ты'), Commands.communication)
    search_google = key_word(('найди', 'поищи'), Commands.search_google)
    say_time = key_word(('время', 'времени', 'час', 'часов', 'дата', 'число', 'дату', 'день'), Commands.say_time)
    get_weather = key_word(('погода', 'погоду', 'погоды', 'прогноз'), Commands.get_weather)
    simple_math = key_word(('+', '-', '*', '/', 'плюс', 'минус', 'умнож', 'умножить',
                            'подели', 'раздели'), Mathematics.simple_math)
    math_sqrt = key_word(('корень', ''), Mathematics.math_sqrt)
    math_exp = key_word(('степень', 'степени', 'квадрат', 'куб'), Mathematics.math_exp)
    run_app = key_word(('включи', 'запусти', 'открой'), Commands.run_app)

    key_words = (communication, search_google, say_time, get_weather, simple_math, math_sqrt, math_exp, run_app)


def search_command(command):
    text = command.lower().split(" ")

    def search(words, i=0):
        if i <= len(words) - 1:
            if set(words[i][0]) & set(text):
                words[i][1](text)
            else:
                search(words, i+1)
        else:
            print('Неизвестная команда')
            Voice.say('Неизвестная команда')
    search(KeyWord.key_words)


if __name__ == '__main__':
    print('Слушаю')
    Voice.say('Слушаю')
    while True:
        user_command = input()
        if len(user_command.replace(' ', '')) == 0:
            continue
        search_command(user_command)
