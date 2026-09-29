"""
Given an array arr[] containing integers and an integer k, 
your task is to find the length of the longest subarray where 
the sum of its elements is equal to the given value k. 
If there is no subarray with sum equal to k, return 0.

Examples:

Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
Output: 5
Explanation: Subarrays with sum = -5 are [-5] and [-5, 8, -14, 2, 4]. 
The length of the longest subarray with a sum of -5 is 5.

Input: arr[] = [10, -10, 20, 30], k = 5
Output: 0
Explanation: No subarray with sum = 5 is present in arr[].

Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: 
Subarrays with sum = 15 are [5, 2, 7, 1], 
[10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.
"""

def longestSubarray(arr, k):  
    cum_sum = 0
    max_length = 0
    cum_sum_map = {}
    n = len(arr)

    for i in range(n):
        cum_sum += arr[i]

        if cum_sum == k:
            max_length = i + 1

        if (cum_sum - k) in cum_sum_map:
            max_length = max(max_length, i -  cum_sum_map[cum_sum-k])

        if cum_sum not in cum_sum_map:
            cum_sum_map[cum_sum]  = i

    return max_length


arr= [10, -10, 20, 30]
k = 50
print(longestSubarray(arr,k))