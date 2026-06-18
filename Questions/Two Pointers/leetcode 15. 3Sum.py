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
"""
# ---------------------------------------------------------------------

# APPROACH 1: Brute Force Solution(3 loops)
"""
KEY IDEA:
- Just check EVERY possible triplet (i,j,k)
- If sum == 0, sort it and store in a SET
  (set automatically removes duplicate triplets)

CODE LOGIC:
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if nums[i]+nums[j]+nums[k] == 0:
                sort & add to set

WHY USE SET + SORT?
- [-1,-1,2] and [-1,2,-1] are SAME triplet
- Sorting makes them look identical
- Set removes exact duplicates automatically

Time:  O(n^3)  -> 3 nested loops
Space: O(no. of triplets) -> for storing results

PROBLEM: Too slow for large arrays
"""

def threeSum_Brute_Force(nums):

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

# ---------------------------------------------------------------------

# APPROACH 2: Better Solution (Hashing) - 2 loops
"""
KEY IDEA:
- Fix one number (nums[i])
- For the remaining pair, instead of using a 3rd loop,
  use a SET to check if the "needed number" exists

LOGIC:
- We need: nums[i] + nums[j] + k = 0
- So:      k = -(nums[i] + nums[j])
- Check if "k" was already seen before (in new_set)
- If yes -> we found a triplet!

CODE LOGIC:
for i in range(n):
    new_set = set()          # reset for each i
    for j in range(i+1, n):
        k = -(nums[i] + nums[j])
        if k in new_set:
            triplet found! sort & add to result set
        new_set.add(nums[j])  # remember this number for future j

WHY new_set RESETS EVERY i?
- Because k depends on nums[i], so the "seen numbers"
  must be specific to current i

Time:  O(n^2)   -> 2 loops, set lookup is O(1)
Space: O(n) for new_set + O(no. of triplets) for result

BETTER than brute force, but still uses extra set space
"""

def threeSum_Better(nums):
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

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum_Brute_Force(nums))
print(threeSum_Better(nums))

# ---------------------------------------------------------------------
# APPROACH 3: Optimal Solution (Sorting + Two Pointer) 

"""
KEY IDEA:
- FIRST sort the array
- Fix one element nums[i]
- For remaining part, use TWO POINTERS (left=j, right=k)
  to find pair that sums to -nums[i]
- Skip duplicates to avoid repeated triplets

WHY SORT FIRST?
- Sorting lets us use two-pointer technique
- Sorting also makes duplicate-skipping easy
  (duplicates sit next to each other)

CODE LOGIC:
sort(nums)

for i in range(n):
    if i>0 and nums[i]==nums[i-1]:
        continue          # skip duplicate "i"

    j = i+1
    k = n-1

    while j < k:
        total = nums[i]+nums[j]+nums[k]

        if total < 0:
            j += 1         # sum too small, increase it
        elif total > 0:
            k -= 1          # sum too big, decrease it
        else:
            store [nums[i],nums[j],nums[k]]
            j += 1
            k -= 1

            # skip duplicates for j and k
            while j<k and nums[j]==nums[j-1]: j+=1
            while j<k and nums[k]==nums[k+1]: k-=1

------------------------------------------
WHY SKIP DUPLICATES? (Important!)
------------------------------------------
- After sorting, same numbers sit together
  e.g. [-2,-2,-2,-1,-1,-1,0,0,0,0,2,2,2,2]
- If we don't skip, we'll add SAME triplet
  [-2,0,2] multiple times
- "if i>0 and nums[i]==nums[i-1]: continue"
   -> skip same starting number
- Same logic applied to j and k after finding a match

"""
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

nums = [-2,-2,-2,-1,-1,-1,0,0,0,0,2,2,2,2]
print(threeSum_Optimal(nums))


"""
DRY RUN (short)

nums sorted = [-4,-1,-1,0,1,2]

i=0 (-4): j=1,k=5 -> sum=-4-1+2=-3 (too small) j++
          j=2,k=5 -> sum=-4-1+2=-3 j++
          j=3,k=5 -> sum=-4+0+2=-2 j++
          j=4,k=5 -> sum=-4+1+2=-1 j++ ... no match for -4

i=1 (-1): j=2,k=5 -> sum=-1-1+2=0 -> [-1,-1,2]
          move j++, k--
i=2 (-1): same as previous i -> SKIP (duplicate)

i=3 (0):  j=4,k=5 -> sum=0+1+2=3 (too big) k--... eventually
          [-1,0,1] found 

Final result: [[-1,-1,2],[-1,0,1]]

COMPLEXITY

Time:  O(n^2)
       -> O(n log n) for sorting
       -> O(n) outer loop * O(n) two-pointer = O(n^2)
       -> overall O(n^2) dominates

Space: O(1) extra (ignoring output array)
       -> sorting may take O(log n) or O(n) depending on language,
          but no extra hashset needed (unlike Approach 2)

          
==========================================
COMPARISON TABLE
==========================================
Approach       | Time     | Space
---------------|----------|------------------
Brute Force    | O(n^3)   | O(triplets)
Better (Hash)  | O(n^2)   | O(n) + O(triplets)
Optimal (2ptr) | O(n^2)   | O(1) + O(triplets)


==========================================
PATTERN TO REMEMBER
==========================================
"Sort + Fix one element + Two Pointer on rest"
-> Useful for problems asking about:
   - Pairs/Triplets with target sum
   - 4Sum (fix two elements, two-pointer on rest)
   - Closest sum problems
"""