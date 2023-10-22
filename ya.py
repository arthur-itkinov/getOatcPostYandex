import yadisk
import datetime
import os
import shutil
import telebot
from telegram import send_msg


now = datetime.datetime.now()
today = datetime.datetime.now()
delta = datetime.timedelta(days=90)
dateback = today - delta
dayback = dateback.strftime("%d")
monthback = dateback.strftime("%m")
yearback = dateback.strftime("%Y")
# мой токен

y = yadisk.YaDisk(
    token="###")


def send_message_telegram(path):
    if y.exists(f'{path}'):
        text = f"Записи разговоров за {dayback}-{monthback}-{yearback} загружены в каталог ЯДиск/OATC/{dayback}-{monthback}-{yearback}"
        send_msg(text)
    else:
        text = f"Записи разговоров за {dayback}-{monthback}-{yearback} НЕ загружены"
        send_msg(text)


# создаю папку на яндекс диске в папке OATC
y.mkdir(f'OATC/{dayback}-{monthback}-{yearback}')
# прохожусь по файлам папки с файлами и отправляю в соответствеющую папку на яндекс диске.
directory = f'{dayback}-{monthback}-{yearback}'


def send_file_yadisk():
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        if os.path.isfile(file):
            y.upload(file, f'/OATC/{dayback}-{monthback}-{yearback}/{file}')
    send_message_telegram(
        f'/OATC/{dayback}-{monthback}-{yearback}/')
    shutil.rmtree(f'{dayback}-{monthback}-{yearback}')


send_file_yadisk()
