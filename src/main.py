import os
import sys
import webbrowser
import math
import time
import random
import json
import pyttsx3
import threading
import speech_recognition
from collections import namedtuple


class Assistant:
    with open("config.json", "r", encoding='utf-8') as file:
        data = json.load(file)

    city = data.get('city')
    voice = bool(data.get('voice'))

    spotify = data.get('spotify')
    telegram = data.get('telegram')
    browser = data.get('browser')
    office = data.get('office')

    answers = {
        'hi': ('Здраствуй!', 'Приветствую!', 'Здраствуйте!', 'Доброго времени суток!'),
        'bye': ('До встречи!', 'Прощайте!', 'До новых встреч!', 'До свидания!'),
        'grat': ('Пожалуйста!', 'Всегда пожалуйста!', 'Обращайтесь!', 'Рада помочь!'),
        'execution': ('Выполняю!', 'Прошу!', 'Конечно!')
    }

    answer = ''


class Voice:

    @staticmethod
    def say(string):

        def engine_start(text):
            if Assistant.voice:
                engine = pyttsx3.init()
                engine.say(text)
                engine.runAndWait()
            else:
                return

        start = threading.Thread(target=engine_start, args=[string])
        start.start()

    @staticmethod
    def say_num(string):
        if string % 1 != 0:
            result = round(string, 2)
            split_num = str(result).split('.')
            Voice.say(f'{split_num[0]},{split_num[1]}')
        else:
            Voice.say(int(string))

    @staticmethod
    def listen():
        mic = speech_recognition.Microphone()
        recognizer = speech_recognition.Recognizer()

        with mic:
            try:
                audio = recognizer.listen(mic, 5, 5)
                result = recognizer.recognize_google(audio, language="ru-RU").lower()
                return result
            except speech_recognition.UnknownValueError:
                Assistant.answer = 'Повторите пожалуйста'
                Voice.say('Повторите пожалуйста')
                return ''
            except speech_recognition.RequestError:
                Assistant.answer = 'Проверьте подключение к интернету'
                Voice.say('Проверьте подключение к интернету')
                return ''
            except speech_recognition.WaitTimeoutError:
                Assistant.answer = 'Проверьте микрофон'
                Voice.say('Проверьте микрофон')
                return ''


class Commands:

    @staticmethod
    def communication(text):
        hi_key_words = ('привет', 'приветствую')
        bye_key_words = ('пока', 'прощай')
        grat_key_words = ('спасибо', 'благодарю')
        info_key_words = ('кто', '  ')
        command_key_words = ('делаешь', 'умеешь', 'можешь', 'ты')

        if bool(set(hi_key_words) & set(text)):
            answer = random.choice(Assistant.answers.get('hi'))
            Assistant.answer = answer
            Voice.say(answer)
        elif bool(set(bye_key_words) & set(text)):
            answer = random.choice(Assistant.answers.get('bye'))
            Voice.say(answer)
            sys.exit()
        elif bool(set(grat_key_words) & set(text)):
            answer = random.choice(Assistant.answers.get('grat'))
            Assistant.answer = answer
            Voice.say(answer)
        elif bool(set(info_key_words) & set(text)):
            Assistant.answer = f'Я Кэролайн, ваш личный голосовой ассистент'
            Voice.say(f'Я Кэролайн, ваш личный голосовой ассистент')
        elif bool(set(command_key_words) & set(text)):
            Assistant.answer = 'Затрудняюсь ответить, меня постоянно улучшают'
            Voice.say('Затрудняюсь ответить, меня постоянно улучшают')

    @staticmethod
    def search_google(text):
        if len(text) == 1:
            Assistant.answer = 'Что именно вы хотите найти?'
            Voice.say('Что именно вы хотите найти?')
            return
        text.pop(0)
        search_query = ' '.join(text)
        url = 'https://google.com/search?q=' + search_query
        answer = random.choice(Assistant.answers.get('execution'))
        Assistant.answer = answer
        Voice.say(answer)
        webbrowser.get().open(url)

    @staticmethod
    def say_time(text):
        time_word = ('время', 'времени', 'час', 'часов')
        full_date_word = ('дата', 'дату')

        if bool(set(time_word) & set(text)):
            Assistant.answer = time.strftime('%H:%M', time.localtime())
            Voice.say(time.strftime('%H:%M', time.localtime()))
        elif bool(set(full_date_word) & set(text)):
            Assistant.answer = time.strftime('%d.%m.%Y', time.localtime())
            Voice.say(time.strftime('%d/%m/%Y', time.localtime()))
        elif 'число' in text:
            Assistant.answer = time.strftime('%m.%d', time.localtime())
            Voice.say(time.strftime('%m/%d', time.localtime()))
        elif 'день' in text:
            Assistant.answer = time.strftime('%A', time.localtime())
            Voice.say(time.strftime('%A', time.localtime()))

    @staticmethod
    def get_weather(text):
        black_list = ('покажи', 'прогноз', 'в', 'погода', 'погоду', 'погоды', 'пожалуйста', 'мне')
        clear_text = list(filter(lambda item: item not in black_list, text))

        if len(clear_text) == 0 and Assistant.city == '':
            Assistant.answer = 'Укажите город'
            Voice.say('Укажите город')
        elif len(clear_text) == 0:
            answer = random.choice(Assistant.answers.get('execution'))
            Assistant.answer = answer
            Voice.say(answer)
            url = 'https://google.com/search?q=' + f'погода  в {Assistant.city}'
            webbrowser.get().open(url)
        else:
            answer = random.choice(Assistant.answers.get('execution'))
            Assistant.answer = answer
            Voice.say(answer)
            url = 'https://google.com/search?q=' + f'погода  в {clear_text[0]}'
            webbrowser.get().open(url)

    @staticmethod
    def run_app(text):
        black_list = ('открой', 'запусти', 'пожалуйста', 'будь', 'добра')
        clear_text = list(filter(lambda item: item not in black_list, text))

        if len(clear_text) == 0:
            Assistant.answer = 'Укажите приложение'
            Voice.say('Укажите приложение')
            return

        try:
            spotify = ('spotify', Assistant.spotify)
            telegram = ('telegram', Assistant.telegram)
            browser = ('браузер', Assistant.browser)
            office = ('офис', Assistant.office)

            apps = (spotify, telegram, browser, office)

            for app in apps:
                if clear_text[0] == app[0]:
                    if app[1] == '':
                        Assistant.answer = 'Приложение не установленно'
                        Voice.say('Приложение не установленно')
                        return
                    else:
                        answer = random.choice(Assistant.answers.get('execution'))
                        Assistant.answer = answer
                        Voice.say(answer)
                        os.startfile(app[1])
                        return

            Assistant.answer = 'Приложение не найденно'
            Voice.say('Приложение не найденно')

        except FileNotFoundError:
            Assistant.answer = 'Указан неверный путь к приложению'
            Voice.say('Указан неверный путь к приложению')

    @staticmethod
    def coin(x):
        flip = round(random.random())

        if flip == 1:
            Assistant.answer = 'Орёл'
            Voice.say('Орёл')
        else:
            Assistant.answer = 'Решка'
            Voice.say('Решка')

    @staticmethod
    def yes_or_no(x):
        rand_answer = round(random.random())

        if rand_answer == 1:
            Assistant.answer = 'Да'
            Voice.say('Да')
        else:
            Assistant.answer = 'Нет'
            Voice.say('Нет')


class Mathematics:

    @staticmethod
    def simple_math(text):
        multi_word = ('умнож', 'умножить', '*', 'х', 'x')
        div_word = ('подели', 'раздели', '/')
        sum_word = ('плюс', '+')
        sub_word = ('минус', '-')
        num = list(map(lambda x: x.replace(',', '.'), text))
        num = list(map(float, filter(lambda x: x.replace('.', '').isdigit(), num)))
        if len(num) == 1:
            Assistant.answer = 'Не хватает аргумента'
            Voice.say('Не хватает аргумента')
            return
        if len(num) == 0:
            Assistant.answer = 'Укажите аргументы'
            Voice.say('Укажите аргументы')
            return

        result = ''

        if bool(set(multi_word) & set(text)):
            result = (num[0] * num[1])
        elif bool(set(div_word) & set(text)):
            if num[1] == 0:
                Assistant.answer = 'Делить на 0 нельзя!!!'
                Voice.say('Делить на 0 нельзя!')
                return
            else:
                result = (num[0] / num[1])
        elif bool(set(sum_word) & set(text)):
            result = (num[0] + num[1])
        elif bool(set(sub_word) & set(text)):
            result = (num[0] - num[1])

        if result % 1 == 0:
            Assistant.answer = round(result)
        else:
            Assistant.answer = result
        Voice.say_num(result)

    @staticmethod
    def math_sqrt(text):
        try:
            num = list(map(float, filter(lambda x: x.replace('.', '').isdigit(), text)))
            result = math.sqrt(num[0])

            if result % 1 == 0:
                Assistant.answer = round(result)
            else:
                Assistant.answer = result
            Voice.say_num(result)

        except IndexError:
            Assistant.answer = 'Укажите аргумент'
            Voice.say('Укажите аргумент')
            return

    @staticmethod
    def math_exp(text):
        try:
            num = list(map(float, filter(lambda x: x.replace('.', '').isdigit(), text)))

            if 'квадрат' in text:
                result = (num[0]**2)
            elif 'куб' in text:
                result = (num[0]**3)
            else:
                result = (num[0]**num[1])

            if result % 1 == 0:
                Assistant.answer = round(result)
            else:
                Assistant.answer = result
            Voice.say_num(result)

        except IndexError:
            Assistant.answer = 'Укажите аргумент'
            Voice.say('Укажите аргумент')
            return


class KeyWord:
    key_word = namedtuple('key_word', 'word func')

    communication = key_word(('привет', 'приветствую', 'пока', 'прощай', 'спасибо', 'благодарю', 'делаешь',
                              'умеешь', 'можешь', 'кто', 'ты'), Commands.communication)
    search_google = key_word(('найди', 'поищи'), Commands.search_google)
    say_time = key_word(('время', 'времени', 'час', 'часов', 'дата', 'число', 'дату', 'день'), Commands.say_time)
    get_weather = key_word(('погода', 'погоду', 'погоды', 'прогноз'), Commands.get_weather)
    simple_math = key_word(('+', '-', '*', '/', 'плюс', 'минус', 'умножь', 'умножить',
                            'подели', 'раздели', 'х', 'x'), Mathematics.simple_math)
    math_sqrt = key_word(('корень', 'корень'), Mathematics.math_sqrt)
    math_exp = key_word(('степень', 'степени', 'квадрат', 'куб'), Mathematics.math_exp)
    run_app = key_word(('включи', 'запусти', 'открой'), Commands.run_app)
    coin = key_word(('монетка', 'монетку', 'монета', 'монету'), Commands.coin)
    yes_or_no = key_word(('да', 'нет'), Commands.yes_or_no)

    key_words = (search_google, simple_math, math_sqrt, math_exp, communication, say_time, get_weather, run_app, coin,
                 yes_or_no)


def search_command(command):
    text = command.lower().split(" ")
    if text[0] == '':
        return

    def search(words, i=0):
        if i <= len(words) - 1:
            if set(words[i][0]) & set(text):
                words[i][1](text)
            else:
                search(words, i+1)
        else:
            Assistant.answer = 'Неизвестная команда'
            Voice.say('Неизвестная команда')
            return
    search(KeyWord.key_words)


def input_text(user_command):
    if len(user_command.replace(' ', '')) == 0:
        return
    search_command(user_command)
    return Assistant.answer


def input_voice():
    user_command = Voice.listen()
    search_command(user_command)
    return Assistant.answer
