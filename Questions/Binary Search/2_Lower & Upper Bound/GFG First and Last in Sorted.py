# link :- https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1

"""
Given a sorted array arr[] with possibly some duplicates, 
find the first and last occurrences of an element x in the given array.
Note: If the number x is not found in the array then return both the indices as -1.

Examples: 1

Input: arr[] = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5
Output: [2, 5]
Explanation: First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5

Examples: 2

Input: arr[] = [1, 3, 5, 5, 5, 5, 7, 123, 125], x = 7
Output: [6, 6]
Explanation: First and last occurrence of 7 is at index 6

Examples: 3

Input: arr[] = [1, 2, 3], x = 4
Output: [-1, -1]
Explanation: No occurrence of 4 in the array, so, output is [-1, -1]

"""


def find(arr, x):
    n = len(arr)

    # lower Bound
    left = 0
    right = n - 1
    lb = -1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= x:
            lb = mid
            right = mid - 1

        else:
            left = mid + 1

    # Upper Bound
    left = 0
    right = n - 1
    ub = -1

    while left <= right:

        mid = (left + right ) // 2
        if arr[mid] <= x:
            ub = mid
            left = mid + 1

        else:
            right = mid - 1

    if lb == -1 or arr[lb] != x:
        return [-1,-1]

    return [lb,ub]

arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
x = 5
print(find(arr,x))