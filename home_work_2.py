file = open('train.csv', 'r').readlines()
male = 0
female = 0

array = []

for line in range(1, len(file)):
    array = file[line].strip().split(',')
    if array[1] == '1' and array[5] == 'male':
        male += 1
    if array[1] == '1' and array[5] == 'female':
        female += 1

print('Выжившие мужчины:', male)
print('Выжившие женщины:', female)

