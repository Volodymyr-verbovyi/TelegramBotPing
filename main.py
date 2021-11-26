import time

import ping3
import telebot
from ping3 import ping

import config

# !/usr/bin/env python2.5
from threading import Thread
import subprocess
from queue import Queue

bot = telebot.TeleBot(config.token)  # запрашиваем конфиг для получения номера токена

num_threads = 4
queue = Queue()
ips = ["192.168.88.120", "10.0.1.3", "10.0.1.11", "10.0.1.51"]


# wraps system ping command
def pinger(i, q):
    """Pings subnet"""
    while True:
        ip = q.get()
        print("Thread %s: Pinging %s" % (i, ip))
        ret = subprocess.call("ping -c 1 %s" % ip,
                              shell=True,
                              stdout=open('/dev/null', 'w'),
                              stderr=subprocess.STDOUT)
        if ret == 0:
            print("%s: is alive" % ip)
        else:
            print("%s: did not respond" % ip)
        q.task_done()


# Spawn thread pool
for i in range(num_threads):
    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()
# Place work in queue
for ip in ips:
    queue.put(ip)
# Wait until worker threads are done to exit
queue.join()


# def uptime_bot():
#     while True:
#         try:
#             if ping('192.168.88.120') is None:
#                 print(f"offline для")
#                 bot.send_message(393645188,
#                                  'Ip не пингуется')
#             else:
#                 ping('192.168.88.120')
#                 # print(f"OHлайн Else для")
#                 # bot.send_message(393645188,
#                 #                  'Пингуеться и все ок')
#
#         except ping3.errors.PingError:
#             print(f'Ошибка совсем')
#             bot.send_message(393645188,
#                              'Вообще Исключение')
#
#         time.sleep(60)
#
#
# if __name__ == '__main__':
#     uptime_bot()
