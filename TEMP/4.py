#разворот массива через второй массив и через while
mass1 = [1, 2, 3, 4, 5, 6]
mass2 = [0, 0, 0, 0, 0, 0]
size = len(mass1)
index = 0
index_r = size - 1
while index < size:
    mass2[index] = mass1[index_r]
    index = index + 1
    index_r = index_r - 1
mass1 = mass2
print(mass1)


