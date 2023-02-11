#нахождение суммы чисел между макс и мин индексами
mass = [12, 1, 10001, 20, 6]
size = len(mass)
index_max = index_min = 0
sum = 0
for index in range(0, size):
    if mass[index] > mass[index_max]:
        index_max = index
    elif mass[index] < mass[index_min]:
        index_min = index
print('индекс мин элемента =', index_min, ', индекс макс элемента =', index_max)
if index_max > index_min:
    start_index = index_min
    end_index = index_max
else:
    start_index = index_max
    end_index = index_min
for index in range(start_index + 1, end_index):
    sum = sum + mass[index]
print('сумма элементов между макс и мин индексами =', sum)