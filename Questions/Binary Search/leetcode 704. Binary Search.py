"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

"""

# TC - O(n logn) | SC - O(1)
def search(nums, target):
    n = len(nums)
    low = 0
    heigh = n - 1

    while low <= heigh:
        mid = (low + heigh) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            heigh = mid - 1

        else:
            low = mid + 1

nums = [5,6,7,8,9,10,15,17,27,35,37,39,48,59,78]
target = 27
print(search(nums,target))