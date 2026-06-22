"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, 
an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""


def findPeakElement(arr):
    left = 0
    right = len(arr) - 1

    while left < right:            # strict less than — stops when converged

        mid = (left + right) // 2

        if arr[mid] <= arr[mid + 1]:
            left = mid + 1          # safe, mid is NOT the peak

        else:
            right = mid             #  mid COULD be peak, don't skip it

    return left                     # left == right == peak index
                     

arr = [1,2,1,3,5,6,4]
print(findPeakElement(arr))

"""
The Rule of Thumb

When using right = mid (not mid - 1), always use left < right, not left <= right.

These two styles must be paired correctly:
# Style 1 — converging
while left < right:
    right = mid        # mid could be answer

# Style 2 — classic
while left <= right:
    right = mid - 1    # mid already checked

"""