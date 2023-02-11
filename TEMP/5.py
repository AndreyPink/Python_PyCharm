numbers = [0, 0, 0]
size = 3
g = 0
result = 3
while g < 3:
    while numbers[g] < result:
        numbers[g] = numbers[g] + 1
    g = g + 1
print('зачет')
