def bubble_sort_assending_order(array):
    n = len(array)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array



def bubble_sort_Desending_order(array):
    n  = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] < array[j+1]:
                array[j],array[j+1]  = array[j+1], array[j]

    return array

array = [5, 9, 3, 10, 45, 2, 0]

print(bubble_sort_assending_order(array))

print(bubble_sort_Desending_order(array))