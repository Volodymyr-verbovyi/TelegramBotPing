import urllib

import ping3
from ping3 import ping

import config
import telebot
import time

bot = telebot.TeleBot(config.token)  # запрашиваем конфиг для получения номера токена


def uptime_bot(urlSite):
    while True:
        try:
            # conn = urllib.request.urlopen(urlSite)
            conn = ping('urlSite') is None
            print(f"offline для" + conn)
            bot.send_message(393645188,
                             'Сервер ОФлайн')

        except :
            print(f'{urlSite} поднят')
            bot.send_message(393645188,
                             'Сервер Онлайн')
        # except urllib.error.HTTPError as e:
        #     # Отправка admin / log
        #     print(f'HTTPError: {e.code} для {urlSite}')
        #     bot.send_message(393645188,
        #                      'Сервер ОФнлайн')
        # except urllib.error.URLError as e:
        #     # Отправка admin / log
        #     print(f'URLError: {e.code} для {urlSite}')
        #     bot.send_message(393645188, 'Сервер ')
        # else:
        #     # Сайт поднят
        #     print(f'{urlSite} Ничего не подошло')
        #     bot.send_message(393645188,
        #                      'Сервер Онлайн')
        time.sleep(15)


if __name__ == '__main__':
    # url = 'http://www.google.com/py'
    url = '192.168.88.120'
    uptime_bot(url)
