# link :- https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1

"""
Given a sorted array arr[] and an integer x,
find the index (0-based) of the largest element in arr[] that is less than or equal to x.
This element is called the floor of x. If such an element does not exist, return -1.

Note: In case of multiple occurrences of floor of x, return the index of the last occurrence.

Examples:- 1

Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 5
Output: 1
Explanation: Largest number less than or equal to 5 is 2, whose index is 1.

Examples:- 2

Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 11
Output: 4
Explanation: Largest Number less than or equal to 11 is 10,
whose indices are 3 and 4. The index of last occurrence is 4.

Examples:- 3

Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 0
Output: -1
Explanation: No element less than or equal to 0 is found. So, output is -1.
"""

"Find :- findout the Largest NO. But Lower than Integer X"

" Solution:- Solve Binary Search :- "
"ans already define -1 becouse in case the X is not present that list they return ans(mens -1)"
"if present - follow the binary search"

def findFloor(arr, x):
    left = 0
    right = len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans

arr= [1, 2, 8, 10, 10, 12, 19] 
x = 11

print(findFloor(arr,x))