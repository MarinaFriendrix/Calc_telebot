from datetime import datetime as dt

def log(data):
    time = dt.now().strftime('%d %B %Y / %H:%M')
    with open('log.txt', 'a') as file:
        file.write('\n' + data + ' ' + time)