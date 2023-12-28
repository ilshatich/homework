import re
def find(string):
    return re.findall(pattern='\\(\w+\\)', string=string)
print(find())