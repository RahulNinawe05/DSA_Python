"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""

# Brutforce Solution
# TC: O(n) | SC: O(n)
#  SPACE NEED

def moveZeroes_BruteForce(nums):
     temp = []

     for num in nums:
          if num != 0:
               temp.append(num)

     for i in range(len(temp)):
          nums[i] = temp[i]

     for j in range(len(temp), len(nums)):
          nums[j] = 0

     return nums


# Better Solution 
# TC: O(n) | SC: O(1)

def moveZeroes_Better(nums):
     j = 0

     for i in range(len(nums)):
          if nums[i] != 0:
               nums[j] = nums[i]
               j += 1

     while j < len(nums):
          nums[j] = 0
          j += 1

     return nums


# Optimal Solution 
#TC: O(n) | SC: O(1)

def moveZeroes_Optimal(nums):
    j = 0

    for i in range(0,len(nums)):
         if nums[i] != 0:
              nums[j] = nums[i]
              j += 1

    for k in range(j,len(nums)):
         nums[k] = 0
         
    return nums

nums = [2,0,3,0,1,5,0]
print(moveZeroes_BruteForce(nums))
print(moveZeroes_Better(nums))
print(moveZeroes_Optimal(nums))