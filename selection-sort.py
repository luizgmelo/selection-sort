def selection_sort(array):
    length = len(array)
    for j in range(0, length):
        min = array[j]
        min_index = j
        for i in range(j, length):
            if array[i] < min:
                min = array[i]
                min_index = i
            
        array[j], array[min_index] = array[min_index], array[j]

random = [5, 2, 3, 1, 4]
reverse = [5, 4, 3, 2, 1]
order = [1, 2, 3, 4, 5]
selection_sort(reverse)
selection_sort(random)
selection_sort(order)
print(reverse)
print(random)
print(order)


