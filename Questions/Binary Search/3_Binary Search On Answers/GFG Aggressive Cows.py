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

def aggressiveCows_BruteForce_Solution(arr, k):
    arr.sort()

    best = 0
    n = len(arr) - 1

    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                d1 = arr[j] - arr[i]
                d2 = arr[k] - arr[j]

                min_dist = min(d1,d2)
                best = max(best,min_dist)

    return best

# arr = [10, 1, 2, 7, 5]
# k = 3

# # arr = [1, 2, 4, 8, 9]
# # k = 3

# # print(aggressiveCows_BruteForce_Solution(arr,k))

# arr.sort()
# n = len(arr) - 1
# for i in range(1, max(arr) - min(arr)):




