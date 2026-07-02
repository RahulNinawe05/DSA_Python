"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""

# TC:- O(m*n) | SC:-O(n)

def minEatingSpeed_Brute_Solution(piles,hr):
    n = max(piles)

    for i in range(1,n+1): 
        s = 0
        for x in piles:
            # s = x // i           # x // i  :- Because // rounds DOWN, but we need round UP.
            s += (x + i - 1) // i  # (x + i - 1) // i  :- Add (i−1) before divide to force round UP.

        if s <= hr:
            return i


piles = [3,6,7,11]
hr = 8

print(minEatingSpeed_Brute_Solution(piles,hr))


# TC:- O(n log m) | SC:- O(1)

def minEatingSpeed_Optimal_Solution(nums,hr):
    left = 1
    right = max(nums)

    while left <= right:
        s = 0
        mid = (left + right) // 2

        for x in nums:
            s += (x + mid - 1) // mid

        if s <= hr:
            right = mid - 1
        else:
            left = mid + 1

    return right

print(minEatingSpeed_Optimal_Solution(piles,hr))

# ============================================================
# PROBLEM : Koko Eating Bananas (LeetCode #875)
# APPROACH: Binary Search on Answer
# TIME    : O(n log m)  |  n = len(piles), m = max(piles)
# SPACE   : O(1)
# ============================================================
 
# ------------------------------------------------------------
# DRY RUN
# Input : piles = [3, 6, 7, 11], h = 8
# Goal  : Find minimum speed k such that Koko finishes in h hours
#
# Initial State:
#   left  = 1
#   right = max(piles) = 11
#
# ── Iteration 1 ─────────────────────────────────────────────
#   mid = (1 + 11) // 2 = 6
#   s   = ceil(3/6) + ceil(6/6) + ceil(7/6) + ceil(11/6)
#       =    1      +     1     +     2      +     2      = 6
#   s=6 <= h=8  → valid speed → try slower → right = 6-1 = 5
#   State: left=1, right=5
#
# ── Iteration 2 ─────────────────────────────────────────────
#   mid = (1 + 5) // 2 = 3
#   s   = ceil(3/3) + ceil(6/3) + ceil(7/3) + ceil(11/3)
#       =    1      +     2     +     3      +     4      = 10
#   s=10 > h=8  → too slow → go faster → left = 3+1 = 4
#   State: left=4, right=5
#
# ── Iteration 3 ─────────────────────────────────────────────
#   mid = (4 + 5) // 2 = 4
#   s   = ceil(3/4) + ceil(6/4) + ceil(7/4) + ceil(11/4)
#       =    1      +     2     +     2      +     3      = 8
#   s=8 <= h=8  → valid speed → try slower → right = 4-1 = 3
#   State: left=4, right=3
#
# ── Loop Ends ────────────────────────────────────────────────
#   left(4) > right(3) → exit
#   return left = 4  ✅
#
# Answer: 4 bananas/hour
# ------------------------------------------------------------