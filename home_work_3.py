file = open('file.xml', 'r', encoding='utf-8').readlines()
count = 0
for line in file:
    if 'http' in line:
        count+= 1
print(count)