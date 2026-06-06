""" 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

# brute Force Solution
# Tc- O(n ^ 2), SC- O(1)

"""
i have to used two for loop
i = 1st loop 0 to len(n) & 
j = 2nd loop i + 1 to len(n)
compaire with target
return index i & j
"""

def brute_Two_Sum(nums,target):
    n = len(nums)
    for i in range(0,n):    
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return i, j

nums = [23,50,56,49]
target = 99
print(brute_Two_Sum(nums,target))


# Optimal Solution
# TC-O(n) , SC - O(n)

""" 
the value of compliment in check in hash_dict 
if it exists return index stored in hash_dict and current index.
else to store in hash_dict with its index as a value (currnt index)
"""
def Optimal_Two_Sum(nums, target):
    n = len(nums)
    hash_dict = {}
    for i in range(0,n):
        compliment = target - nums[i]
        if compliment in hash_dict:
            return hash_dict[compliment],  i 
        hash_dict[nums[i]] = i

print(Optimal_Two_Sum(nums,target))

"""
i checked compliment in hash_dict(all keys) write as this 'hash_dict.keys()' - Syntax Probleme
i am returning current index & keys in hash_dict(Not a value)   
"""