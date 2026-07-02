# link - https://www.geeksforgeeks.org/problems/ceil-in-a-sorted-array/1

"""
Given a sorted array arr[] and an integer x, 
find the index (0-based) of the smallest element in arr[] that is greater than or equal to x. 
This element is called the ceil of x. If such an element does not exist, return -1.

Note: In case of multiple occurrences of ceil of x, return the index of the first occurrence.

Examples -1

Input: arr[] = [1, 2, 8, 10, 11, 12, 19], x = 5
Output: 2
Explanation: Smallest number greater than 5 is 8, whose index is 2.

Examples -2 

Input: arr[] = [1, 2, 8, 10, 11, 12, 19], x = 20
Output: -1
Explanation: No element greater than 20 is found. So output is -1.

Examples -3
Input: arr[] = [1, 1, 2, 8, 10, 11, 12, 19], x = 0
Output: 0
Explanation: Smallest number greater than 0 is 1, 
whose indices are 0 and 1. The index of the first occurrence is 0.

"""

"Find :- findout the smallest NO. But Greater than Integer X"

" Solution:- Solve Binary Search :- "
"ans already define -1 becouse in case the X is not present that list they return ans(mens -1)"
"if present - follow the binary search"

def findCeil(arr, x):
    left = 0
    right = len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= x:
            ans = mid
            right = mid - 1

        else:
            left = mid + 1

    return ans

arr= [1, 2, 8, 10, 11, 12, 19]
x = 5

print(findCeil(arr,x))


def lower(nums,x):
    left = 0
    right = len(nums) - 1
    ans1 = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= x:
            ans = mid
            right = mid - 1

        else:
            left = mid + 1

    return ans

def upper(nums,x):
    left = 0
    right = len(nums) - 1
    ans2 = -1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] <= x:
            ans2 = mid
            left = mid + 1

        else:
            right = mid - 1

    return ans2



nums = [1, 3, 5, 5, 5, 5, 67, 123, 125]
x = 5

print(lower(nums,x))
print(upper(nums,x))