# -*- coding: utf-8 -*-

import bot
import time
import weather


class Pogodnik:
    def __init__(self):
        self.token = bot.token

    def start_bot(self, none_stop=True):
        bot.bot.polling(none_stop)

    @bot.bot.message_handler(commands=['ten_weather'])
    def send_ten_weather(msg):
        while True:
            w = weather.Weather()
            w.prepare_weather()
            bot.bot.send_message(msg.chat.id, w)
            time.sleep(600)
            del w

    @bot.bot.message_handler(commands=['once_weather'])
    def send_once_weather(msg):
        w = weather.Weather()
        w.prepare_weather()
        bot.bot.send_message(msg.chat.id, w)
        del w