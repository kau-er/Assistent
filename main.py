import os
import random
import speech_recognition
import datetime


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

commands_dict = {
    'commands': {
        'greeting': ['привет', 'здравствуй'],
        'create_task': ['заметки', 'заметка', 'запись', 'запись текста'],
        'play_music': ['музыка', 'послушать', 'слушать музыку']
    }
}

def listen_command():
    """Единая функция распознания всех команд"""
    try:
        """Распознание команды"""
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query

    except speech_recognition.UnknownValueError:
        return 'Damn...не распознано'


def greeting():
    """Функция приветствия"""
    return 'Я вас категорически приветствую!'


def create_task():
    """Функция заметок"""
    print("Что добавим в заметки")

    query = listen_command()

    with open('list.txt', 'a') as file:
        now = datetime.datetime.now()
        now = now.strftime("%d-%m-%Y %H:%M")
        file.write(f'{now}:  {query}\n')

    return f'Заметка добавлена в файл с меткой {now}'

def play_music():
    """"Функция запускае музыку"""
    way = 'C:/Users/user/Desktop/Музыка/Rammstein/Mutter_2001'
    files = os.listdir(way)
    random_files = f'{way}/{random.choice(files)}'
    k = f'start {random_files}'
    print(k)
    os.system(k)
    return f'музыка для вас'



def main():
    query = ""
    while query !='выход':
        query = listen_command()
        print(query)

        for k, v in commands_dict['commands'].items():
            if query in v:
                print(globals()[k]())


if __name__ == '__main__':
    main()