list_numbers = [9, 8, 10, 2, 6]
size = len(list_numbers)
index = 0
while index < size - 1:
    if list_numbers[index] > list_numbers[index+1]:
        list_numbers.append(list_numbers[index])
        del list_numbers[index]
        index = 0
    else:
        index = index + 1
print(list_numbers)