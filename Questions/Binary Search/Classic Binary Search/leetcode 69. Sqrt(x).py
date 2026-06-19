"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., 
and since we round it down to the nearest integer, 2 is returned.
"""

# Brute Force Solution - Linear Search 
# In this 5^2 = 25 means 5 ** 5 but in this question i want to find squreroot of 25
# so that is start form 0 in every itreation compare with x
# multiplication of {i} ** {i} is less than x

# problems =
# If x = 1,000,000 you loop 1000 times
# If x = 2,000,000,000 you loop 44,721 times
# Gets very slow for large inputs

# TC:- O(n) | SC:- O(1)
def mySqrt_Brute(x):
    i = 0
    while i * i <= x:
        i += 1
    return i - 1


# TC:- O(log n)   |   SC:- O(1)
def mySqrt_Optimal(x):
    low = 0
    high = x

    while low <=  high:
        mid = (low + high) // 2
        if mid * mid == x:
            return mid

        elif mid * mid > x:
            high= mid - 1

        else:
            low = mid + 1

    # return -1 # wrong ans 
    return high

x = 1000
print(mySqrt_Brute(x))

print(mySqrt_Optimal(x))

# wrong ans :- dry run

# # x = 8 ke liye trace karo:
# low=0, high=8 → mid=4 → 16 > 8  → high=3
# low=0, high=3 → mid=1 → 1  < 8  → low=2
# low=2, high=3 → mid=2 → 4  < 8  → low=3
# low=3, high=3 → mid=3 → 9  > 8  → high=2

# low(3) > high(2) → loop ends → returns -1 ❌******
# Correct answer = 2 ✅  (high return)