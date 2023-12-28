import re
string = re.findall(pattern=(r'\b[А-ЯЁA-Z][a-zA-Zа-яА-ЯёЁ]+'), string='Вауцфав Defqw цыв')
print(string)