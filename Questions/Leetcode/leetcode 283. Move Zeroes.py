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

def moveZeroes_BruteForce(nums):
    zero_store = []
    number_store = []
    for i in range(0,len(nums)):
            if nums[i] <= 0:
                 zero_store.append(nums[i])
            else:
                  number_store.append(nums[i])
    return number_store + zero_store # store the both Of addition so sc - O(n)


# Optimal Solution 
#TC: O(n) | SC: O(1)

"""
Approach (Two-Pass / Overwrite Technique)
This is a slightly different two-pointer style than the swap version. 
Instead of swapping, it works in two passes:

First pass: Walk through the array and copy every non-zero element to the front, 
compacting them together (overwriting as you go). j tracks how many non-zero elements have been placed.

Second pass: Once all non-zero elements are compacted at the front (positions 0 to j-1), 
fill everything from j to the end with 0s.

This works because after the first loop, the first j positions contain all non-zero values in order — but 
some of them might be "duplicated" (overwritten copies still sitting from earlier), 
so the second loop cleans up the tail by zeroing it out.
"""
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
print(moveZeroes_Optimal(nums))