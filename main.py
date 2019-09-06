# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from wxpy import *
from platform import system
import time
from importlib import reload
from plugins import config
from random import choice


class MyRobot:
    def __init__(self):
        if 'Windows' in system():
            self.bot = Bot()
        elif 'Darwin' in system():
            self.bot = Bot()
        elif 'Linux' in system():
            self.bot = Bot(console_qr=2, cache_path=True)
        else:
            print("cannot determine your system!!")
        self.friend = self.bot.friends().search(self.config.wechat_name)[0]

        self.config = config.Config()

    def reload(self):
        reload(config)
        self.config = config.Config()

    def send_message(self, msg):
        self.friend.send(msg)

    def care(self):
        now_time = time.ctime()[-13:-8]
        print(now_time)
        if now_time == self.config.morning_time:
            self.send_message(choice(self.config.str_list_good_morning))


bot = ''
friend = ''
if __name__ == "__main__":
    my_robot = MyRobot()
    bot = my_robot.bot
    friend = my_robot.friend
    while True:
        my_robot.reload()
        my_robot.care()
        time.sleep(60)


@bot.register(chats=friend, except_self=False)
def on_receive(msg):
    print(msg.text)
    # call chat robot api
    reply = ""
    friend.send(reply)

