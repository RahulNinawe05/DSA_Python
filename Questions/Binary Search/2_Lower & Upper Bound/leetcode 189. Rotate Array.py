"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100
"""
# Find the Rotete the list k times from right side

# Approch 1:- firstly the list converted in reverse order

# why use this k = k % n becouse in this minimize the retation,
# how:- if n = 7 (len of nums), & k= 0,7,14,... all the value are same list
# ex:-
# k=0  →  [1,2,3,4,5,6,7]  (original)
# k=7  →  [1,2,3,4,5,6,7]  (same as k=0)
# k=14 →  [1,2,3,4,5,6,7]  (same as k=0)
# you used this k = k % n , so actually - k = 10 % 7 = 3 means (if k = 3 similar to k=10) don't extra ratation
# # Rotating 10 times == Rotating 3 times (saves 7 useless steps)

# Reversed the (0 - k) -> after that (k - n)

def rotate(nums, k):

    n = len(nums)

    k = k % n
    nums.reverse()

    nums[:k] = reversed(nums[:k])

    nums[k:] = reversed(nums[k:])

    return nums


# Approch 2:- 1) reverse list
#             2) 0 - k => reverse using slicing
#             2) 1 by 1 => reverse using for loop

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate(nums, k))


def rotate_Brute(nums, k):

    nums.sort(reverse=True)

    nums[:k] = reversed(nums[:k])

    for i in range(k, len(nums)):
        re = nums.pop()
        nums.insert(i, re)

    return nums


print(rotate_Brute(nums, k))
