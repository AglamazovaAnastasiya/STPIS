import datetime

def get_current_time():
    return datetime.datetime.now()

def format_date(date):
    return date.strftime("%Y-%m-%d %H:%M:%S")
