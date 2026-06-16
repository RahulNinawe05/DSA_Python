# TC =  (n-1) + (n-2) + .....+ 2 + 1
#    =  n(n-1)/2
#    = n^2/2 - n/2
#    = O(n^2) 

# SC = O(1)

def bubble_sort_assending_order(array):
    n = len(array)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

# array = [5, 9, 3, 10, 45, 2, 0]   n = 7

# ── PASS i=5 → j = 0,1,2,3,4,5 ─────────────────────────────
# j=0:  5 >  9 ? NO  → [5,  9,  3, 10, 45,  2,  0]
# j=1:  9 >  3 ? YES → [5,  3,  9, 10, 45,  2,  0]
# j=2:  9 > 10 ? NO  → [5,  3,  9, 10, 45,  2,  0]
# j=3: 10 > 45 ? NO  → [5,  3,  9, 10, 45,  2,  0]
# j=4: 45 >  2 ? YES → [5,  3,  9, 10,  2, 45,  0]
# j=5: 45 >  0 ? YES → [5,  3,  9, 10,  2,  0, 45] ← 45 ✓

# ── PASS i=4 → j = 0,1,2,3,4 ───────────────────────────────
# j=0:  5 >  3 ? YES → [3,  5,  9, 10,  2,  0, 45]
# j=1:  5 >  9 ? NO  → [3,  5,  9, 10,  2,  0, 45]
# j=2:  9 > 10 ? NO  → [3,  5,  9, 10,  2,  0, 45]
# j=3: 10 >  2 ? YES → [3,  5,  9,  2, 10,  0, 45]
# j=4: 10 >  0 ? YES → [3,  5,  9,  2,  0, 10, 45] ← 10 ✓

# ── PASS i=3 → j = 0,1,2,3 ─────────────────────────────────
# j=0:  3 >  5 ? NO  → [3,  5,  9,  2,  0, 10, 45]
# j=1:  5 >  9 ? NO  → [3,  5,  9,  2,  0, 10, 45]
# j=2:  9 >  2 ? YES → [3,  5,  2,  9,  0, 10, 45]
# j=3:  9 >  0 ? YES → [3,  5,  2,  0,  9, 10, 45] ← 9 ✓

# ── PASS i=2 → j = 0,1,2 ────────────────────────────────────
# j=0:  3 >  5 ? NO  → [3,  5,  2,  0,  9, 10, 45]
# j=1:  5 >  2 ? YES → [3,  2,  5,  0,  9, 10, 45]
# j=2:  5 >  0 ? YES → [3,  2,  0,  5,  9, 10, 45] ← 5 ✓

# ── PASS i=1 → j = 0,1 ──────────────────────────────────────
# j=0:  3 >  2 ? YES → [2,  3,  0,  5,  9, 10, 45]
# j=1:  3 >  0 ? YES → [2,  0,  3,  5,  9, 10, 45] ← 3 ✓

# ── PASS i=0 → j = 0 ────────────────────────────────────────
# j=0:  2 >  0 ? YES → [0,  2,  3,  5,  9, 10, 45] ← 2 ✓


# tc = 
def bubble_sort_Desending_order(array):
    n  = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] < array[j+1]:
                array[j],array[j+1]  = array[j+1], array[j]

    return array

array = [5, 9, 3, 10, 45, 2, 0]

print(bubble_sort_assending_order(array))

print(bubble_sort_Desending_order(array))


#  Optimize Best Case to O(n)
# tc = O(n)
# sc = O(1)  extra boolean
def bubble_sort_Descending_optimized(array):
    n = len(array)
    for i in range(n-1):
        swapped = False

        for j in range(0,n-1-i):
            if array[j] < array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    return array

array = [45,34,23,12,13,9,8,7,6,5]

print(bubble_sort_Descending_optimized(array))