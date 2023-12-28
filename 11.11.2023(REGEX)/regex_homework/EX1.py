import re
string = input()
if re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', string):
    print('Частный')
elif re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}\b', string):
    print('Такси')
else:
    print("Не номер")