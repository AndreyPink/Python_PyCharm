#нахождение индексов максимального и минимального числа массива
# mass = [12, 18000, 15, 20, 60000]
# size = len(mass)
# index_max = index_min = 0
# for index in range(0, size):
#     if mass[index] > mass[index_max]:
#         index_max = index
#     elif mass[index] < mass[index_min]:
#         index_min = index
# print('индекс мин элемента =', index_min, ', индекс макс элемента =', index_max)


mass = [12, 10000, 15, 20, 60000]
size = len(mass)
index = 1
index_max = index_min = 0
while index < size:
    if mass[index] >= mass[index_max]:
        index_max = index
    elif mass[index] < mass[index_min]:
        index_min = index
    index += 1
print('индекс мин элемента =', index_min, ', индекс макс элемента =', index_max)

sum = 0
if index_max > index_min:
    start_index = index_min + 1
    end_index = index_max
else:
    start_index = index_max + 1
    end_index = index_min
while start_index < end_index:
    sum = sum + mass[start_index]
    start_index += 1
print('сумма элементов между макс и мин индексами =', sum)