import re

string = input()
print(len(re.split(r'\W+[-\W]*', string)))
