# Merge To Sorted Array

arr = [93,6,8,1,2,6,9,8,4,9,3,2,0,9,45,889,333,54]



def merge_sorted(left,right):

    result = []
    n,m = len(left),len(right)
    i,j = 0,0

    while i < n and j < m:
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j += 1

    if i < n:
        while i < n:
            result.append(left[i])
            i += 1

    if j < m:
        while j < m:
            result.append(right[j])
            j += 1
    return result


def merge_array(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_halt = arr[mid:]
    left_side = merge_array(left_half)
    right_side = merge_array(right_halt)

    return merge_sorted(left_side,right_side)

print(merge_array(arr))



# # =============================================================================
# DRY RUN — Merge To Sorted Array (Merge Sort)
# =============================================================================
# arr = [93,6,8,1,2,6,9,8,4,9,3,2,0,9,45,889,333,54]
# len(arr) = 18
#
# ─────────────────────────────────────────────────────────────────────────────
# HIGH-LEVEL IDEA
# ─────────────────────────────────────────────────────────────────────────────
# merge_array()   → Recursively split array in half until each piece is 1 element
# merge_sorted()  → Merge two already-sorted halves into one sorted array
#
# ─────────────────────────────────────────────────────────────────────────────
# STEP 1 — RECURSIVE SPLITTING TREE
# ─────────────────────────────────────────────────────────────────────────────
#
#  [93,6,8,1,2,6,9,8,4 | 9,3,2,0,9,45,889,333,54]   mid = 9
#            ↙                         ↘
#  [93,6,8,1 | 2,6,9,8,4]       [9,3,2,0 | 9,45,889,333,54]   mid = 4 / 4
#      ↙          ↘                  ↙              ↘
# [93,6|8,1]  [2,6|9,8,4]      [9,3|2,0]    [9,45|889,333,54]  mid = 2 / 2
#  ↙    ↘      ↙    ↘            ↙   ↘        ↙       ↘
# [93] [6] [8] [1] [2,6] [9,8,4] [9,3] [2,0] [9,45] [889,333,54]
#                   ↙ ↘  ↙    ↘   ↙↘   ↙↘    ↙  ↘    ↙       ↘
#                  [2][6][9][8,4] [9][3][2][0][9][45] [889] [333,54]
#                           ↙↘                               ↙     ↘
#                          [8][4]                          [333]   [54]
#
# Base case: len(arr) <= 1 → return as-is (single elements are "sorted")
#
# ─────────────────────────────────────────────────────────────────────────────
# STEP 2 — MERGING (bottom-up, showing key merges)
# ─────────────────────────────────────────────────────────────────────────────
#
# merge_sorted([L], [R]):
#   Compare L[i] vs R[j] → append smaller → advance that pointer
#   Drain remaining elements once one side is exhausted
#
# ── LEFT BRANCH ─────────────────────────────────────────────────────────────
#
# merge_sorted([93], [6])
#   i=0,j=0 → 93 >= 6  → append 6, j=1
#   j exhausted         → append 93
#   result → [6, 93]
#
# merge_sorted([8], [1])
#   i=0,j=0 → 8 >= 1   → append 1, j=1
#   j exhausted         → append 8
#   result → [1, 8]
#
# merge_sorted([6,93], [1,8])
#   i=0,j=0 → 6 >= 1   → append 1, j=1
#   i=0,j=1 → 6 < 8    → append 6, i=1
#   i=1,j=1 → 93 >= 8  → append 8, j=2
#   j exhausted         → append 93
#   result → [1, 6, 8, 93]           ← sorted [93,6,8,1]
#
# merge_sorted([2], [6])  → [2, 6]
#
# merge_sorted([8], [4])
#   8 >= 4 → append 4; drain → append 8
#   result → [4, 8]
#
# merge_sorted([9], [4,8])
#   9 >= 4 → append 4, j=1
#   9 >= 8 → append 8, j=2
#   j exhausted → append 9
#   result → [4, 8, 9]
#
# merge_sorted([2,6], [4,8,9])
#   2 < 4   → append 2, i=1
#   6 >= 4  → append 4, j=1
#   6 < 8   → append 6, i=2
#   i exhausted → drain [8, 9]
#   result → [2, 4, 6, 8, 9]         ← sorted [2,6,9,8,4]
#
# merge_sorted([1,6,8,93], [2,4,6,8,9])
#   1 < 2   → append 1,  i=1
#   6 >= 2  → append 2,  j=1
#   6 >= 4  → append 4,  j=2
#   6 >= 6  → append 6,  j=3   ← equal: right is preferred (else branch)
#   6 < 8   → append 6,  i=2
#   8 >= 8  → append 8,  j=4   ← equal again: right preferred
#   8 < 9   → append 8,  i=3
#   93 >= 9 → append 9,  j=5
#   j exhausted → append 93
#   result → [1, 2, 4, 6, 6, 8, 8, 9, 93]    ← LEFT SIDE DONE ✓
#
# ── RIGHT BRANCH ────────────────────────────────────────────────────────────
#
# merge_sorted([9], [3])  → [3, 9]
# merge_sorted([2], [0])  → [0, 2]
#
# merge_sorted([3,9], [0,2])
#   3 >= 0 → append 0, j=1
#   3 >= 2 → append 2, j=2
#   j exhausted → drain [3, 9]
#   result → [0, 2, 3, 9]
#
# merge_sorted([9], [45]) → [9, 45]
#
# merge_sorted([333], [54])
#   333 >= 54 → append 54, j=1; drain → append 333
#   result → [54, 333]
#
# merge_sorted([889], [54,333])
#   889 >= 54  → append 54,  j=1
#   889 >= 333 → append 333, j=2
#   j exhausted → append 889
#   result → [54, 333, 889]
#
# merge_sorted([9,45], [54,333,889])
#   9  < 54  → append 9,  i=1
#   45 < 54  → append 45, i=2
#   i exhausted → drain [54, 333, 889]
#   result → [9, 45, 54, 333, 889]
#
# merge_sorted([0,2,3,9], [9,45,54,333,889])
#   0 < 9   → append 0,  i=1
#   2 < 9   → append 2,  i=2
#   3 < 9   → append 3,  i=3
#   9 >= 9  → append 9,  j=1    ← right preferred on equal
#   9 < 45  → append 9,  i=4
#   i exhausted → drain [45,54,333,889]
#   result → [0, 2, 3, 9, 9, 45, 54, 333, 889]   ← RIGHT SIDE DONE ✓
#
# ─────────────────────────────────────────────────────────────────────────────
# STEP 3 — FINAL MERGE
# ─────────────────────────────────────────────────────────────────────────────
#
# LEFT  = [1, 2, 4, 6, 6, 8, 8, 9, 93]
# RIGHT = [0, 2, 3, 9, 9, 45, 54, 333, 889]
#
# i=0,j=0  → 1 >= 0      → append 0,   j=1
# i=0,j=1  → 1 < 2       → append 1,   i=1
# i=1,j=1  → 2 >= 2      → append 2,   j=2   ← right preferred (equal)
# i=1,j=2  → 2 < 3       → append 2,   i=2
# i=2,j=2  → 4 >= 3      → append 3,   j=3
# i=2,j=3  → 4 < 9       → append 4,   i=3
# i=3,j=3  → 6 < 9       → append 6,   i=4
# i=4,j=3  → 6 < 9       → append 6,   i=5
# i=5,j=3  → 8 < 9       → append 8,   i=6
# i=6,j=3  → 8 < 9       → append 8,   i=7
# i=7,j=3  → 9 >= 9      → append 9,   j=4   ← right preferred (equal)
# i=7,j=4  → 9 >= 9      → append 9,   j=5   ← right preferred (equal)
# i=7,j=5  → 9 < 45      → append 9,   i=8
# i=8,j=5  → 93 >= 45    → append 45,  j=6
# i=8,j=6  → 93 >= 54    → append 54,  j=7
# i=8,j=7  → 93 < 333    → append 93,  i=9
# i exhausted → drain [333, 889]
#
# ─────────────────────────────────────────────────────────────────────────────
# FINAL OUTPUT
# ─────────────────────────────────────────────────────────────────────────────
#
# [0, 1, 2, 2, 3, 4, 6, 6, 8, 8, 9, 9, 9, 45, 54, 93, 333, 889]
#
# ─────────────────────────────────────────────────────────────────────────────
# COMPLEXITY SUMMARY
# ─────────────────────────────────────────────────────────────────────────────
#
# Time  → O(n log n)
#          log₂(18) ≈ 4.17  →  ~4-5 levels of recursion
#          Each level does O(n) = O(18) comparisons
#
# Space → O(n)  — `result` lists created at each merge level
#
# ─────────────────────────────────────────────────────────────────────────────
# ONE KEY BEHAVIOUR TO NOTE
# ─────────────────────────────────────────────────────────────────────────────
#
# The `else` branch in merge_sorted handles the EQUAL case:
#   if left[i] < right[j]:   ← strictly less than
#       ...
#   else:                     ← includes left[i] == right[j]
#       append right[j]       ← right element is always preferred on tie
#
# This makes the sort STABLE for right-side elements on duplicates.
# (Duplicates in result: 2 appears twice, 6 twice, 8 twice, 9 three times)
#
# =============================================================================