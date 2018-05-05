# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup


class Weather:
    def __init__(self):
        self.weather = {}

    def get_page(self, page):
        with urllib.request.urlopen(page) as raw_data:
            self.page = BeautifulSoup(raw_data.read().decode('utf-8').encode('utf-8'), 'html.parser')

    def get_param(self, tag, _class):
        return self.page.find(tag, {'class':_class}).text

    def set_param(self, param_name, param_val):
        self.weather[param_name] = param_val

    def prepare_weather(self):
        self.get_page('https://yandex.ru/pogoda/ulyanovsk/')
        self.set_param('temp', self.get_param('div', 'current-weather__thermometer current-weather__thermometer_type_now'))
        self.set_param('comment', self.get_param('span', 'current-weather__comment'))
        self.set_param('wind_speed', self.get_param('span', 'wind-speed'))
        self.set_param('wind_direction', self.get_param('abbr', ' icon-abbr'))

    def __str__(self):
        return self.weather['temp'] + ', ' + self.weather['comment'] + '. Ветер: ' + self.weather['wind_direction'] + ', ' + self.weather['wind_speed'] + '.'