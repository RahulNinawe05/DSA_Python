"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""

# TC :- O(n)  |  SC :- O(1)

# firsty  my thought process is  (arr = [-1,1,2,3,4,5,6,7,7,7,8,9,20]) go linear  1 by 1 after that if nums[i] == target & nums[i] != nums[i - 1]  add start go forword
# otherwise :- at the end of , if nums[i] != nums[i+1] and nums[i] == target :- go forword
# but 1 problem , what was => i am ittreting one by one but i am access i + 1 ,
# but the loop to len(n) they are thoroughing error msg, if i used len(n) - 1 after that last no. are ignore it that's why i chosse anather

#  already define start & end (-1) if condition start == -1 so start replace with i , else in every ittreation end change
# if condition is nums[i] != target & start != -1 they breadk it  

def searchRange_Brute_Solution(nums,target):
    start = -1
    end = -1
    n = len(nums) 
    for i in range(0,n):
        if nums[i] == target:
            if start == -1:
                start = i
            end = i
        elif start != -1:   # nums[i] != target 
            break
    return (start,end)

# Optimal Solution 

# TC :- O(n log n) + O(n log n) = O(log n)  |   SC :- O(1) 



def lower_bound(nums, target):
    left = 0
    right = len(nums) - 1
    ans = len(nums)

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

def upper_bound(nums, target):
    left = 0
    right = len(nums) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

class Solution:
    def countFreq(self, arr, target):
        lb = lower_bound(arr, target)
        ub = upper_bound(arr, target)

        if lb == len(arr) or arr[lb] != target:
            return [-1,-1]

        return ub - lb

arr = [-1,1,2,3,4,5,6,7,7,7,8,9,20]
target = 5

print(Solution().countFreq(arr, target))