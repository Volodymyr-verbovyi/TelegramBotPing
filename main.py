import time

import ping3
import telebot
from ping3 import ping

import config

bot = telebot.TeleBot(config.token)  # запрашиваем конфиг для получения номера токена


def uptime_bot():
    while True:
        try:
            if ping('192.168.88.120') is None:
                print(f"offline для")
                bot.send_message(393645188,
                             'Ip не пингуется')
            else:
                ping('192.168.88.120')
                # print(f"OHлайн Else для")
                # bot.send_message(393645188,
                #                  'Пингуеться и все ок')

        except ping3.errors.PingError:
            print(f'{urlSite} Ошибка совсем')
            bot.send_message(393645188,
                             'Вообще Исключение')

        time.sleep(5)


if __name__ == '__main__':
    # url = 'http://www.google.com/py'
    urlSite = '192.168.88.120'
    uptime_bot()
