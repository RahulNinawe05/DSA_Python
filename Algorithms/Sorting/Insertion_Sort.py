# TC :- 
# Best case: O(n)
# Average case: O(n²)
# Worst case: O(n²)

# SC :- O(1)
def Insertion_Sort(nums):
    n = len(nums)
    for i in range(1,n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] >key:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = key

    return nums

nums = [3,5,6,4,8,9,10,7,1]
print(Insertion_Sort(nums))


# nums = [3, 5, 6, 4, 8, 9, 10, 7, 1]
# n = 9  →  outer loop: i goes  1 → 2 → 3 → 4 → 5 → 6 → 7 → 8

#  # ── i=1  key=5  j=0 ──────────────────────────────────────────
# nums[0]=3 > 5 ? NO  → place key at j+1=1
# [3, 5, 6, 4, 8, 9, 10, 7, 1]  ← no change

# ── i=2  key=6  j=1 ──────────────────────────────────────────
# nums[1]=5 > 6 ? NO  → place key at j+1=2
# [3, 5, 6, 4, 8, 9, 10, 7, 1]  ← no change

# ── i=3  key=4  j=2 ──────────────────────────────────────────
# nums[2]=6 > 4 ? YES → shift: nums[3]=6,  j=1  → [3, 5, 6, 6, 8, 9, 10, 7, 1]
# nums[1]=5 > 4 ? YES → shift: nums[2]=5,  j=0  → [3, 5, 5, 6, 8, 9, 10, 7, 1]
# nums[0]=3 > 4 ? NO  → place key at j+1=1
# [3, 4, 5, 6, 8, 9, 10, 7, 1]  ✅ 4 inserted

# ── i=4  key=8  j=3 ──────────────────────────────────────────
# nums[3]=6 > 8 ? NO  → place key at j+1=4
# [3, 4, 5, 6, 8, 9, 10, 7, 1]  ← no change

# ── i=5  key=9  j=4 ──────────────────────────────────────────
# nums[4]=8 > 9 ? NO  → place key at j+1=5
# [3, 4, 5, 6, 8, 9, 10, 7, 1]  ← no change

# ── i=6  key=10  j=5 ─────────────────────────────────────────
# nums[5]=9 > 10 ? NO  → place key at j+1=6
# [3, 4, 5, 6, 8, 9, 10, 7, 1]  ← no change

# ── i=7  key=7  j=6 ──────────────────────────────────────────
# nums[6]=10 > 7 ? YES → shift: nums[7]=10, j=5  → [3, 4, 5, 6, 8, 9, 10, 10, 1]
# nums[5]= 9 > 7 ? YES → shift: nums[6]=9,  j=4  → [3, 4, 5, 6, 8, 9,  9, 10, 1]
# nums[4]= 8 > 7 ? YES → shift: nums[5]=8,  j=3  → [3, 4, 5, 6, 8, 8,  9, 10, 1]
# nums[3]= 6 > 7 ? NO  → place key at j+1=4
# [3, 4, 5, 6, 7, 8, 9, 10, 1]  ✅ 7 inserted

# ── i=8  key=1  j=7 ──────────────────────────────────────────
# nums[7]=10 > 1 ? YES → shift: nums[8]=10, j=6  → [3, 4, 5, 6, 7, 8,  9, 10, 10]
# nums[6]= 9 > 1 ? YES → shift: nums[7]=9,  j=5  → [3, 4, 5, 6, 7, 8,  9,  9, 10]
# nums[5]= 8 > 1 ? YES → shift: nums[6]=8,  j=4  → [3, 4, 5, 6, 7, 8,  8,  9, 10]
# nums[4]= 7 > 1 ? YES → shift: nums[5]=7,  j=3  → [3, 4, 5, 6, 7, 7,  8,  9, 10]
# nums[3]= 6 > 1 ? YES → shift: nums[4]=6,  j=2  → [3, 4, 5, 6, 6, 7,  8,  9, 10]
# nums[2]= 5 > 1 ? YES → shift: nums[3]=5,  j=1  → [3, 4, 5, 5, 6, 7,  8,  9, 10]
# nums[1]= 4 > 1 ? YES → shift: nums[2]=4,  j=0  → [3, 4, 4, 5, 6, 7,  8,  9, 10]
# nums[0]= 3 > 1 ? YES → shift: nums[1]=3,  j=-1 → [3, 3, 4, 5, 6, 7,  8,  9, 10]
# j=-1 → STOP  → place key at j+1=0
# [1, 3, 4, 5, 6, 7, 8, 9, 10]  ✅ 1 inserted