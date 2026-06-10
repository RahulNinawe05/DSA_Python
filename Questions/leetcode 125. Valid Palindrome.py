""" 
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

"""

# Problem: Valid Palindrome
# Approach: Clean string first, then use Two Pointer technique
# Time: O(n) | Space: O(n)

def isPalindrome(s):
    result = ""

    # Step 1: Keep only alphanumeric chars and convert to lowercase
    for ch in s:
        if ch.isalnum(): # ignore spaces, commas, colons etc.
            result += ch.lower()

    # Step 2: Two pointers - one from start, one from end
    left = 0
    right = len(result) - 1

    # Step 3: Compare characters from both sides moving inward
    while left < right:
        if result[left] != result[right]: # mismatch found → not palindrome
            return False
        left += 1 # move inword
        right -= 1 # move inward

    return True #all chars matched → it's a palindrome

s = "A man aplan, a canal: Panama"
print(isPalindrome(s))


# Wrong
# import re
# s = "A man, a plan, a canal: Panama"
# res = re.sub(r'[^A-Za-z]','',s).lower()
# print(res.lower())

# left = 0
# right = len(res)- 1

# while left < right:
#     if res[left] == res[right]:
#         left += 1
#         right -= 1
#         print("True")
#         break
# print("False")