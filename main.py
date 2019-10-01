# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from wxpy import *
from platform import system
import time
from importlib import reload
from plugins import config
from random import choice
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


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
        self.config = config.Config()
        self.friend = self.bot.friends().search(self.config.wechat_name)[0]
        self.chatbot = ChatBot("ChineseChatbot1")
        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer.train("chatterbot.corpus.chinese")

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


my_robot = MyRobot()
bot = my_robot.bot
friend = my_robot.friend
chatterBot = my_robot.chatbot
@bot.register(friend)
def on_receive(msg):
    print(msg.text)
    # call chat robot api
    reply = chatterBot.get_response(msg.txt)
    print(reply)
    friend.send(reply)

while True:
    my_robot.reload()
    my_robot.care()
    time.sleep(60)




