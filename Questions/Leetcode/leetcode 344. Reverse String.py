"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


"""
APPROACH: Two Pointer (swap from both ends)

KEY IDEA:
- Take one pointer at the START (left)
- Take one pointer at the END (right)
- Swap the characters at left and right
- Move left forward, move right backward
- Stop when left meets or crosses right
  (no need to swap middle element if it's odd length,
   it stays in its place automatically)

COMPLEXITY
Time:  O(n)   -> we touch each element about once
Space: O(1)   -> no extra array, swap happens in-place

"""

def reverseString(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left],s[right] = s[right],s[left]

        left += 1
        right -= 1

    return s

s = ["h","e","l","l","o"]
print(reverseString(s))

"""
DRY RUN

s = ["h","e","l","l","o"]
left=0, right=4

Step 1: swap s[0],s[4] -> ["o","e","l","l","h"]
        left=1, right=3

Step 2: swap s[1],s[3] -> ["o","l","l","e","h"]
        left=2, right=2

Step 3: left == right -> stop loop (middle element stays)

Final: ["o","l","l","e","h"]
------------------------------------------

WHY SWAP TUPLE TRICK WORKS
s[left], s[right] = s[right], s[left]
- Python evaluates the right side first (both old values)
- Then assigns them to left side positions
- So no temp variable needed for swapping

PATTERN TO REMEMBER
"Two Pointer - swap and shrink" is useful when:
- We need to reverse something in-place
- We need to check palindrome
- We need to move elements from both ends toward center

Same pattern family as:
- Reverse Array
- Valid Palindrome
- Squares of Sorted Array (977)
"""