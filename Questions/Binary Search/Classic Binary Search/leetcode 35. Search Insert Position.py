"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""

# 2 Cases hain:

# Case 1: Target MILA array mein   → uska INDEX return karo
# Case 2: Target NAHI mila         → KAHAN insert hoga wo index return karo

# Classic Binary Search hi hai — bas ek twist hai!
# Classic BS:   target nahi mila → return -1
# Is problem:   target nahi mila → return LOW ⬅️ yahi twist hai!

def searchInsert_Optimal(arr,target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] >= target:
            high = mid - 1

        else:
            low = mid + 1

    return low

arr = [1,3,5,6,45,78,90]
target = 55

print(searchInsert_Optimal(arr,target))


"""
# DRY RUN:-
arr = [1, 3, 5, 6, 45, 78, 90]
idx =  0  1  2  3   4   5   6

target = 55,  low=0, high=6

Step 1: mid=3 → arr[3]=6  < 55 → low=4
Step 2: mid=5 → arr[5]=78 > 55 → high=4
Step 3: mid=4 → arr[4]=45 < 55 → low=5

low(5) > high(4) → STOP

return low = 5 ✅

[1, 3, 5, 6, 45, 55, 78, 90]
                  ↑
              index 5 pe insert hoga

"""