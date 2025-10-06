# utils.py - вспомогательные функции

import datetime

def get_current_time():
    return datetime.datetime.now()

def format_date(date):
    return date.strftime("%Y-%m-%d %H:%M:%S")

def get_timestamp():
    return int(datetime.datetime.now().timestamp())
