"""
Idea

Divide sorted array in half → check middle → go left or right → repeat


1. Real Example
Dictionary me word "Mango" dhundna →
- Book ke middle page pe jao
- "Mango" < middle word → left side jao
- Phir half karo → repeat
- Seedha page pe pahuch jao 

2. Coding Problem

Input  → [2, 5, 8, 12, 16, 23, 38, 45]
Target → 23
Output → index 5

Sorted array me target element ka index find karo

3. Iterative Solution Logic
low = 0
high = last index

Step 1 → mid = (low + high) / 2
Step 2 → array[mid] == target → return mid 
Step 3 → target > array[mid]  → low = mid + 1 (go right)
Step 4 → target < array[mid]  → high = mid - 1 (go left)
Step 5 → low > high           → not found → return -1

Example →
[2, 5, 8, 12, 16, 23, 38, 45]  target=23
low=0  high=7  mid=3 → 12 < 23 → go right
low=4  high=7  mid=5 → 23 == 23 → return 5

4. Recursive Solution Logic
Call itself again with smaller array

array[mid] == target → return mid 
target > array[mid]  → call function(mid+1, high)
target < array[mid]  → call function(low, mid-1)
low > high           → return -1

Example →
search(0,7) → mid=3 → 12 < 23 → search(4,7)
search(4,7) → mid=5 → 23 == 23 → return 5


5. TC & SC
          Best    Average   Worst
TC  →     O(1)   O(log n)  O(log n)
Iterative SC → O(1)      no extra memory
Recursive SC → O(log n)  recursive stack
"""

def Inttretion_sort(array,target):
    n = len(array)
    low = 0
    heigh = n - 1
    while low <= heigh:
        mid = (low + heigh)// 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            heigh = mid - 1
    return -1


def Recursive_sort(array,target,low,heigh):
    if low > heigh:
        return -1
    mid =(low + heigh) // 2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return Recursive_sort(array,target,mid+1,heigh)
    else:
        return Recursive_sort(array,target,low,mid-1)



array = [5,6,7,8,9,10,15,17,27,35,37,39,48,59,78]
target = 59

# print(Inttretion_sort(array,target))
print(Recursive_sort(array, target, 0, len(array) - 1))