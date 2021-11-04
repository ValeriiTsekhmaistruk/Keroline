import main
import json
import sys
import os
from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '440')
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox

Window.clearcolor = (40/225, 40/225, 40/225, 1)


class KerolineApp(App):

    def build(self):
        main_bl = BoxLayout(orientation='vertical',
                            padding=10,
                            spacing=5)

        setting_menu_content_bl = BoxLayout(orientation='vertical')
        setting_menu = Popup(title='Настройки', content=setting_menu_content_bl, auto_dismiss=False)

        label_bl = BoxLayout(size_hint=(1, .06))
        text_bl = BoxLayout(size_hint=(1, .48))
        send_bl = BoxLayout(size_hint=(1, .08), spacing=3)
        speak_btn_bl = BoxLayout(size_hint=(1, .29), padding=(80, 4, 80, 4))
        setting_btn_bl = BoxLayout(size_hint=(1, .09))

        name_label = Label(text='KEROLINE',
                           font_size=30)

        self.text_label = Label(text='Cлушаю!', font_size=20,
                                text_size=(300 - 20, 400 * .4 - 20),
                                valign='center',
                                halign='center')

        self.send_input = TextInput(size_hint=(.8, 1),
                                    font_size=15,
                                    multiline=False)

        self.send_btn = Button(size_hint=(.13, 1),
                               background_normal='..//img//send.png',
                               background_down='..//img//send_on.png',
                               border=(0, 0, 0, 0))

        self.speak_btn = Button(background_normal='..//img//mic.png',
                                background_down='..//img//mic_on.png',
                                border=(0, 0, 0, 0))

        self.setitng_btn = Button(text='Настройки')

        label_bl.add_widget(name_label)
        text_bl.add_widget(self.text_label)

        send_bl.add_widget(self.send_input)
        send_bl.add_widget(self.send_btn)

        speak_btn_bl.add_widget(self.speak_btn)

        setting_btn_bl.add_widget(self.setitng_btn)

        main_bl.add_widget(label_bl)
        main_bl.add_widget(text_bl)
        main_bl.add_widget(send_bl)
        main_bl.add_widget(speak_btn_bl)
        main_bl.add_widget(setting_btn_bl)

        setting_menu_bl = BoxLayout(size_hint=(1, .9),
                                    orientation='vertical',
                                    padding=5,
                                    spacing=1)
        setting_menu_btn_bl = BoxLayout(size_hint=(1, .1))

        self.city = TextInput(font_size=11, multiline=False, size_hint=(1, .27), text=main.Assistant.city)
        self.path_spotify = TextInput(font_size=11,multiline=False, size_hint=(1, .27), text=main.Assistant.spotify)
        self.path_telegram = TextInput(font_size=11, multiline=False, size_hint=(1, .27), text=main.Assistant.telegram)
        self.path_browser = TextInput(font_size=11, multiline=False, size_hint=(1, .27), text=main.Assistant.browser)
        self.path_office = TextInput(font_size=11, multiline=False, size_hint=(1, .27), text=main.Assistant.office)
        self.voice_cb = CheckBox(size_hint=(1, .27))
        self.voice_cb.active = main.Assistant.voice

        self.close_setting_btn = Button(text='Выйти')
        self.save_setting_btn = Button(text='Сохранить')

        city_label = Label(text='Ваш город', font_size=12, size_hint=(1, .3), halign='left', text_size=(265, 20))
        spotify_label = Label(text='Spotify', font_size=12, size_hint=(1, .3), halign='left', text_size=(265, 20))
        telegram_label = Label(text='Telegram', font_size=12, size_hint=(1, .3), halign='left', text_size=(265, 20))
        browser_label = Label(text='Браузер', font_size=12, size_hint=(1, .3), halign='left', text_size=(265, 20))
        office_label = Label(text='Office', font_size=12, size_hint=(1, .3), halign='left', text_size=(265, 20))
        voice_label = Label(text='Голос', font_size=15, size_hint=(1, .25))

        setting_menu_bl.add_widget(city_label)
        setting_menu_bl.add_widget(self.city)
        setting_menu_bl.add_widget(spotify_label)
        setting_menu_bl.add_widget(self.path_spotify)
        setting_menu_bl.add_widget(telegram_label)
        setting_menu_bl.add_widget(self.path_telegram)
        setting_menu_bl.add_widget(browser_label)
        setting_menu_bl.add_widget(self.path_browser)
        setting_menu_bl.add_widget(office_label)
        setting_menu_bl.add_widget(self.path_office)
        setting_menu_bl.add_widget(voice_label)
        setting_menu_bl.add_widget(self.voice_cb)

        setting_menu_btn_bl.add_widget(self.save_setting_btn)
        setting_menu_btn_bl.add_widget(self.close_setting_btn)

        setting_menu_content_bl.add_widget(setting_menu_bl)
        setting_menu_content_bl.add_widget(setting_menu_btn_bl)

        def enter_on(instance):
            answer = main.input_text(instance.text.strip())
            if answer:
                self.text_label.text = str(answer)
            instance.text = ''

        def send_btn_on(instance):
            answer = main.input_text(self.send_input.text.strip())
            if answer:
                self.text_label.text = str(answer)
            self.send_input.text = ''

        def speak_btn_on(instance):
            answer = main.input_voice()
            if answer:
                self.text_label.text = str(answer)

        def save_setting_btn_on(instance):
            if self.voice_cb.active:
                voice_value = '1'
            else:
                voice_value = ''

            data = {
                "city": self.city.text,
                "voice": voice_value,

                "spotify": self.path_spotify.text.strip(),
                "telegram": self.path_telegram.text.strip(),
                "browser": self.path_browser.text.strip(),
                "office": self.path_office.text.strip()
            }

            with open("config.json", "w", encoding='utf-8') as write_file:
                json.dump(data, write_file, indent=4, ensure_ascii=False)

            python = sys.executable
            os.execl(python, python, "\"{}\"".format(sys.argv[0]))

        self.send_input.bind(on_text_validate=enter_on)
        self.send_btn.bind(on_press=send_btn_on)
        self.speak_btn.bind(on_release=speak_btn_on)
        self.setitng_btn.bind(on_press=setting_menu.open)
        self.close_setting_btn.bind(on_press=setting_menu.dismiss)
        self.save_setting_btn.bind(on_press=save_setting_btn_on)

        return main_bl


if __name__ == '__main__':
    main.Voice.say('слушаю!')
    KerolineApp().run()
