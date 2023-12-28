import re
def find_caps():
    return re.findall(pattern = r'\b[A-Z,А-Я]+\b',string = 'аааБББввв EFNV 2- frmsgk d1wqqwf')
print(find_caps())