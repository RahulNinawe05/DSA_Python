"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

# Brute Force Solution (3 loops)
# TC - O(n^3) 
# SC- O(n^3) (worst case)

def threeSum_Brute_Solution(nums):
    empty_set = set()

    n = len(nums)
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp_list = [nums[i], nums[j], nums[k]]
                    temp_list.sort()
                    empty_set.add(tuple(temp_list))

    return [list(ans) for ans in empty_set]


# Better Solution (Hashing) - 2 loops
# TC - O(n^2)
# SC - O(n)

def threeSum_Better_Solution(nums):
    result = set()

    for i in range(0, len(nums)):

        new_set = set()

        for j in range(i+1, len(nums)):

            k = -(nums[i] + nums[j])

            if k in new_set:
                temp = [nums[i],nums[j],k]
                temp.sort()
                result.add(tuple(temp))

            new_set.add(nums[j])

    return [list(ans) for ans in result]


# Optimal Solution (Sorting + Two Pointer) 


def threeSum_Optimal(nums):
    result = []
    n = len(nums)
    nums.sort()
    for i in range(0,n):
        if i != 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = n - 1
        while j < k:
            total_sum = nums[i] + nums[j] + nums[k]

            if total_sum < 0:
                j += 1

            elif total_sum > 0:
                k -= 1

            else:
                temp = [nums[i],nums[j],nums[k]]
                result.append(temp)
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j - 1]:
                    j += 1

                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

    return result


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum_Brute_Solution(nums))
print(threeSum_Better_Solution(nums))