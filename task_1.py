array = [1, 3, 6, 7, 8, 2, 5, 9, 4, 10]
temp = 0

#Без цикла for, выводиться числа в порядке возрастания
#sort_array = sorted(array)

#print(sort_array)

for i in range(0, len(array)):
    for j in range(i + 1, len(array)):
        if(array[i] > array[j]):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            
for i in range(0, len(array)):
    print(array[i], end=' ')