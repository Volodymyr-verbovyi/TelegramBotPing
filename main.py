from ping3 import ping
import config
import telebot
import time

bot = telebot.TeleBot(config.token)  # запрашиваем конфиг для получения номера токена

a = 1
i = 0
j = 0
k = 0
b = 0
while b == 1:
    time.sleep(240)  # пауза на 240 секунд, можно сменить на своё значение

if (ping('192.168.88.16') is None):  # тут заместо '192.168.0.0' вводим ip адрес нужного на сервера
    i = 1
else:
    print(i, j)
    if (i == 1 and j == 1):
        i = 0
        j = 0
        print('онлайн')  # Это вывод в консоль что сервер онлайн
        bot.send_message(393645188,
                         'Сервер Онлайн')  # бот отравляет сообщения в телегу юзеру по id 333333333, Текст так-же можно менять
if (i == 1 and j != 1):
    print('Сервер Офлайн')  # Это вывод в консоль что сервер офлайн
    bot.send_message(393645188,
                     'Сервер Офлайн')  # бот отравляет сообщения в телегу юзеру по id 333333333, Текст так-же можно менять.
    if i == 1:
        j = 1
