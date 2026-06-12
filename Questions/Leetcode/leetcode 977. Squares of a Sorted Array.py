"""
Leetcode - 977

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

1 <= nums.length <= 104 
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""

# WHAT IT ASKS:
#   - We get a sorted array (numbers can be negative or positive)
#   - We need to square every number
#   - Then return the squares in sorted (ascending) order

"""
APPROACH 1: Brute Force (Easy way)

Steps:
1. Square every element
2. Sort the result

Time:  O(n log n)  -> because of sorting
Space: O(n)        -> extra array used

This works, but it's not the "best" answer in interviews
because we're not using the fact that input is already sorted.
"""
nums = [-4,-1,0,3,10]

def sortedSquares_Brute_Force(nums):
    result = []
    i = 0
    while i <= len(nums)-1:
        result.append(nums[i] ** 2)

        i += 1
    result.sort()

    return result

""" 
APPROACH 2: Two Pointer (Smart way)

KEY IDEA:
- Since array is sorted, the BIGGEST square value
  will always be at one of the two ends (leftmost
  or rightmost element), because negative numbers
  become positive after squaring.

- So compare nums[left]^2 and nums[right]^2
- Whichever is BIGGER, that goes to the END of result
- Move that pointer inward
- Keep doing this until left > right
- Finally reverse the result (because we filled it
  from biggest to smallest)

"""

def sortedSquares_Optimal(nums):
    result = []
    left = 0
    right = len(nums) - 1
    while left <= right:
        a = nums[left] ** 2
        b = nums[right] ** 2

        if a >= b:
            result.append(a)
            left += 1
        else:
            result.append(b)
            right -= 1

    result.reverse()

    return result


nums = [-4,-1,0,3,10]
print(sortedSquares_Brute_Force(nums))
print(sortedSquares_Optimal(nums))


"""
DRY RUN:
nums = [-4, -1, 0, 3, 10]
left=0(-4), right=4(10)

Step 1: 16 vs 100 -> 100 bigger -> result=[100], right-- 
Step 2: 16 vs 9   -> 16 bigger  -> result=[100,16], left++
Step 3: 1 vs 9    -> 9 bigger   -> result=[100,16,9], right--
Step 4: 1 vs 0    -> 1 bigger   -> result=[100,16,9,1], left++
Step 5: left>right -> stop

Reverse result -> [1,9,16,100,...] 
(wait check final reverse gives [0,1,9,16,100])

Time:  O(n)   -> we just go through array once
Space: O(n)   -> result array

------------------------------------------

WHY TWO POINTER IS BETTER
- Brute force:  O(n log n) because of sort()
- Two pointer:  O(n) - no sorting needed
- Two pointer uses the "sorted array" hint smartly

PATTERN TO REMEMBER
"Two Pointer from both ends" is useful when:
- Array is SORTED
- We need MAX/MIN comparison from both sides
- We want to build result in reverse order

Remember this trick for future problems like:
- Merge sorted arrays
- Container with most water
- Palindrome checks
"""
