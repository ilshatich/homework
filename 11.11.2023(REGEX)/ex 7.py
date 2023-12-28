import re
def time(time):
    return re.findall(pattern=r'([0-1][0-9]|2[0-3]):([0-5][0-9])', string=time)
time()
