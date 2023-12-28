import re

def find_digits():
    return re.findall(pattern='\d', string='124r1d2we123e12e')
print(find_digits())