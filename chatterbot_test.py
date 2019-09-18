# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot("ChineseChatbot1")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.chinese")
question = '早上好'
response = chatbot.get_response(question)
print(question)
print(response)
print("###########################################")
question = "很高兴认识你"
print(question)
print(chatbot.get_response(question))
print("###########################################")
question = "嗨，最近如何?"
print(question)
print(chatbot.get_response(question))
print("###########################################")
question = "复杂优于晦涩"
print(question)
print(chatbot.get_response(question))
print("###########################################")
question = "面对模棱两可，拒绝猜测的诱惑."
print(question)
print(chatbot.get_response(question))
print("###########################################")
question = "生命、宇宙以及世间万物的终极答案是什么?"
print(question)
print(chatbot.get_response(question))
print("###########################################")