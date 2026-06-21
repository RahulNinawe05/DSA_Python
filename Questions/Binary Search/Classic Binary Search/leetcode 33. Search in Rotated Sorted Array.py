"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly low rotated at an unknown index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be low rotated by 3 indices and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""


# TC:- O(n) | SC:- O(n)
def search_Brute(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# TC:- O(log n) | SC:- O(1)
def search_Optimal(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)// 2

        if arr[mid] == target:
            return mid

        if arr[low] <= arr[mid]:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


arr = [10,12,14,16,18,20,8,7]
target = 12
print(search_Brute(arr, target))
print(search_Optimal(arr,target))


# dry run 
# arr = [4, 5, 6, 7, 0, 1, 2]
# index   0  1  2  3  4  5  6
# target = 12

