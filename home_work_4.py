file = open('file.xml', 'r', encoding='utf-8')
lines = file.readlines()
count = 0
for line in lines:
    if 'http' in line:

        end_link = 0
        while line.find('http', end_link) != -1:
            start_link = line.find('http', end_link)
            if line[start_link - 1] == '"':
                end_link = line.find('"', start_link)
            elif line[start_link - 1] == ' ':
                end_link = line.find(' ', start_link)
            else:
                end_link = line.rfind('<')

            count += 1
            print(line[start_link:end_link])

print('Cсылок найдено: ', count)