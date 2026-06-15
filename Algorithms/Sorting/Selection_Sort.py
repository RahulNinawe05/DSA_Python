"""
Selection Sort:
It works by finding the smallest element from the unsorted part
and placing it in the correct position step by step.
"""

# def selection_sort(arr):
#     n = len(arr)          # total number of elements in the list

#     # Outer loop: one element is fixed in its correct position each time
#     for i in range(n):

#         # assume the current index has the smallest value
#         min_index = i

#         # Inner loop: find the smallest element in the remaining list
#         for j in range(i + 1, n):

#             # if current element is smaller than the assumed smallest
#             if arr[j] < arr[min_index]:
#                 min_index = j   # update the index of the smallest element

#         # swap the smallest element with the element at index i
#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr


# array = [5, 9, 3, 10, 45, 2, 0]
# print("Final Sorted Array:", selection_sort(array))
# output - Final Sorted Array: [0, 2, 3, 5, 9, 10, 45]


def selection_decending(array):
    result = []
    for i in range(0,len(array)):
        max_index= i
        for j in range(i+1,len(array)):
            if array[max_index] <= array[j]:
                max_index = j
            array[i],array[max_index] = array[max_index],array[i]

    return array

array = [5, 9, 3, 10, 45, 2, 0]
print("Final Sorted Array:", selection_decending(array))