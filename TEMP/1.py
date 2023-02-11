# сортировка массива данных по возрастанию
mass = [1, 15, 9, 8, 0, 10, 2, 6, 13]
size = len(mass)
index = 0
while index < size - 1:
    if mass[index] > mass[index+1]:
        mass.append(mass[index])
        del mass[index]
        index = 0
    else:
        index = index + 1
print('сортированный массив', mass)
print('мин элемент =', mass[0], ', макс элемент =', mass[size-1])

