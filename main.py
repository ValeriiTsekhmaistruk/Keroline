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
        elif word in thanks:
            print('пожалуйста')
        elif word in how_are_you:
            print('отлично')



commands = {
    ('привет', 'пока', 'спасибо', 'дела'): communication
}


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



