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


arr = [10,12,14,16,18,20,8,9]
target = 12
print(search_Brute(arr, target))
print(search_Optimal(arr,target))


# dry run 
# arr = [10, 12, 14, 16, 18, 20, 8, 7]
# index   0   1   2   3   4   5  6  7
# target = 12

# Iteration 1
# low=0, high=7
# mid = (0+7)//2 = 3
# arr[mid] = arr[3] = 16

# arr[mid] == target?  16 == 12 → NO

# arr[low] <= arr[mid]?
# arr[0]=10 <= arr[3]=16 → YES ✅ → LEFT is sorted

# arr[low] <= target <= arr[mid]?
# 10 <= 12 <= 16 → YES ✅  (target inside left range)

# → high = mid - 1 = 2

# Iteration 2
# low=0, high=2
# mid = (0+2)//2 = 1
# arr[mid] = arr[1] = 12

# arr[mid] == target?  12 == 12 → YES ✅

# → return 1