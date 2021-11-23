import urllib
import config
import telebot
import time

bot = telebot.TeleBot(config.token)  # запрашиваем конфиг для получения номера токена


def uptime_bot(urlSite):
    while True:
        try:
            conn = urllib.request.urlopen(urlSite)
        except urllib.error.HTTPError as e:
            # Отправка admin / log
            print(f'HTTPError: {e.code} для {urlSite}')
            bot.send_message(393645188,
                             'Сервер ОФнлайн')
        except urllib.error.URLError as e:
            # Отправка admin / log
            print(f'URLError: {e.code} для {urlSite}')
            bot.send_message(393645188, 'Сервер ')
        else:
            # Сайт поднят
            print(f'{urlSite} поднят')
            bot.send_message(393645188,
                             'Сервер Онлайн')
        time.sleep(15)


if __name__ == '__main__':
    url = 'http://www.google.com/py'
    uptime_bot(url)
