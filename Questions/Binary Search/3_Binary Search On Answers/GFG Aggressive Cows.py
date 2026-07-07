# Link :- https://www.geeksforgeeks.org/problems/aggressive-cows/1

# Given an integer array arr[], which denotes the positions of stalls. 
# All the positions are distinct. There are k aggressive cows.

# Assign the cows to the stalls such that the minimum distance between any two cows is maximized.

# Examples 1:

# Input: arr[] = [1, 2, 4, 8, 9], k = 3
# Output: 3
# Explanation: The first cow can be placed at arr[0], the second at arr[2], and the third at arr[3]. 
# The minimum distance between any two cows is 3 (between arr[0] and arr[2]), 
# which is the maximum possible among all valid arrangements.

# Examples 2:

# Input: arr[] = [10, 1, 2, 7, 5], k = 3
# Output: 4
# Explanation: The first cow can be placed at arr[0], the second at arr[1], and the third at arr[4]. 
# In this arrangement, the minimum distance between any two cows is 4 (between arr[1] and arr[4]), 
# which is the maximum possible among all valid arrangements.

# Brute Force Solution 

# TC:- O(n^3) | SC:- n(1)

arr = [10, 1, 2, 7, 5]
arr.sort()
k = 3
n = len(arr) 

best = 0

for i in range(n):
    for j in range(i+1,n):
        for l in range(j+1,n):
            # print(arr[i], arr[j], arr[l])

            d1 = arr[j] - arr[i]
            d2 = arr[l] - arr[j]
            # print(d1," ",d2)

            min_dist = min(d1,d2)
            # print(min_dist)

            best = max(best,min_dist)

print(best)


# (1, 2, 4) -> min distance = 1
# (1, 2, 8) -> min distance = 1
# (1, 2, 9) -> min distance = 1
# (1, 4, 8) -> min distance = 3
# (1, 4, 9) -> min distance = 3
# (1, 8, 9) -> min distance = 1
# (2, 4, 8) -> min distance = 2
# (2, 4, 9) -> min distance = 2
# (2, 8, 9) -> min distance = 1
# (4, 8, 9) -> min distance = 1

# Answer = 3


# Optimal Solution 

# TC:- O(n log n) | SC:- O(1)

def aggressiveCows(arr,k):
    arr.sort()

    n = len(arr) 

    left = 1
    right = arr[-1] - arr[0]    # LAST 2nd VALUE

    result = 0

    while left <= right:

        mid = (left + right) // 2

        last_position = arr[0]      # 1
        cows = 1

        for i in range(1, len(arr)):
            if arr[i] - last_position >= mid:   # 
                cows += 1
                last_position = arr[i]

        if cows >= k :
            result = mid
            left = mid + 1

        else:
            right = mid - 1

    return result

arr = [10, 1, 2, 7, 5]
k = 3

print(aggressiveCows(arr,k))

"""
# FOR UNDERSTADING (WHY USE OPTIMAL)
# Step 1: Brute Force Approach

In brute force, we try every possible combination of cow placements.
Example:
(1,2,4) → minimum distance = 1
(1,2,8) → minimum distance = 1
(1,4,8) → minimum distance = 3
(1,4,9) → minimum distance = 3

After checking all combinations:
Maximum minimum distance = 3
Problem:
If n becomes very large (example n = 100000),
number of combinations becomes huge.
So brute force is not efficient.
Time Complexity:
O(n³) for k = 3


# Aggressive Cows - Binary Search on Answer

def aggressiveCows(arr, k)

## Approach:
- Sort the stall positions.
- Search the answer (minimum distance) using Binary Search.
- For each mid distance, use Greedy to check if k cows can be placed.

## Binary Search:
- left = 1 (minimum possible distance)
- right = max stall distance = arr[-1] - arr[0]

## Greedy Check:
- Place first cow at the first stall.
- Traverse the array.
- If current stall - last cow position >= mid:
    - Place next cow.
    - Update last_position.
- Count placed cows.

## Decision:
If cows >= k:
    - Current distance is possible.
    - Store answer.
    - Try bigger distance.

Else:
    - Distance is too large.
    - Try smaller distance.

## Why Binary Search?
Possible distances follow a monotonic pattern:

YES YES YES NO NO NO

Because of this pattern, Binary Search can be applied on the answer space.

## Complexity:
Time Complexity: O(n log D)
Space Complexity: O(1)

D = maximum possible distance between stalls

## Key Idea:
Don't search all cow placements.
Search the maximum possible minimum distance.
"""
