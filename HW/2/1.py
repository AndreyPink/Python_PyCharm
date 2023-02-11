#нахождение индексов максимального и минимального числа массива

mass = [12, 10000, 15, 20, 60000]
size = len(mass)
index = 1
index_max = index_min = 0
while index < size:
    if mass[index] > mass[index_max]:
        index_max = index
    elif mass[index] < mass[index_min]:
        index_min = index
    index = index + 1
print('индекс мин элемента =', index_min, ', индекс макс элемента =', index_max)

print(max(mass))
