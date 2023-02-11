#среднее из элементов массива

mass = [1, 2, 3, 4, 5, 6, 7]
size = len(mass)
index = 0
sum = 0
while index < size:
    sum = sum + mass[index]
    index = index + 1
average = sum / size
print(average)