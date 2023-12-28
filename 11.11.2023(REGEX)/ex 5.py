import re
def find(string):
    return re.findall(pattern='#[0-9a-fAF]{6}', string=string)
print(find())