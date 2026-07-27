"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""


def sortColors_Brute_Force(nums):
    cout_zero= []
    cout_one = []
    cout_two = []
    for i in range(0,len(nums)):
        if nums[i] == 0:
            cout_zero.append(0)
        elif nums[i] == 1:
            cout_one.append(1)
        else:
            cout_two.append(2)

    ind = 0
    for _ in range(len(cout_zero)):
        nums[ind] = 0
        ind += 1

    for _ in range(len(cout_one)):
        nums[ind] = 1
        ind += 1

    for _ in range(len(cout_two)):
        nums[ind] = 2
        ind += 1
    return nums

nums = [2,0,2,1,1,0,1,2,0]

print(sortColors_Brute_Force(nums))


def optimal_solution(arr):
    
    left = 0
    mid = 0
    right = len(arr) - 1

    while mid <= right:

        if arr[mid] == 0:
            arr[left],arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        elif arr[mid] == 2:
            arr[mid], arr[right] = arr[right],arr[mid]
            right -= 1

    return arr

arr = [2,0,2,1,1,0,0,2]
print(optimal_solution(arr))