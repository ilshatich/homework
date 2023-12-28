import re

def find_rus_char():
    return re.findall(pattern=('[а-я, А-Я]+\d+'), string='вторн1 fwkemfw31 аппкп31')
print(find_rus_char())