"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
"""


def findMin_Brute(nums):
    Left = 0
    Right = len(nums) - 1

    while Left < Right:
        mid = (Left + Right) // 2            

        if nums[mid] > nums[Right]:
            Left = mid + 1

        elif nums[mid] <= nums[Right]:
            Right = mid

    return nums[Left]


nums = [5, 6, 7,8,9]
print(findMin_Brute(nums))


"""
Dry Run — nums = [5, 6, 7, 8, 9]

Left  = 0
Right = 4

Iteration 1:-

    Index =  0   1   2   3   4
    nums  = [5,  6,  7,  8,  9]
            L        M        R

    Left=0, Right=4 → 0 < 4 ✅ Enter loop

    mid = (0 + 4) // 2 = 2

    nums[mid]   = nums[2] = 7
    nums[Right] = nums[4] = 9

    7 > 9 ? ❌ NO
    7 ≤ 9 ? ✅ YES → Right = mid = 2


Iteration 2:-

    Index =  0   1   2   3   4
    nums  = [5,  6,  7,  8,  9]
            L   M   R

    Left=0, Right=2 → 0 < 2 ✅ Enter loop

    mid = (0 + 2) // 2 = 1

    nums[mid]   = nums[1] = 6
    nums[Right] = nums[2] = 7

    6 > 7 ? ❌ NO
    6 ≤ 7 ? ✅ YES → Right = mid = 1

Iteration 3:-

    Index =  0   1   2   3   4
    nums  = [5,  6,  7,  8,  9]
            L   R
            M

    Left=0, Right=1 → 0 < 1 ✅ Enter loop

    mid = (0 + 1) // 2 = 0

    nums[mid]   = nums[0] = 5
    nums[Right] = nums[1] = 6

    5 > 6 ? ❌ NO
    5 ≤ 6 ? ✅ YES → Right = mid = 0


Iteration 4:-

    Index =  0   1   2   3   4
    nums  = [5,  6,  7,  8,  9]
            L=R

    Left=0, Right=0 → 0 < 0 ❌ EXIT loop
    """