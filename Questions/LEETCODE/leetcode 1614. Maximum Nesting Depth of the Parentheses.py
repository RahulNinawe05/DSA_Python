"""
Given a valid parentheses string s, return the nesting depth of s. 
The nesting depth is the maximum number of nested parentheses.

Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation:
Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3
Explanation:
Digit 3 is inside of 3 nested parentheses in the string.

Example 3:
Input: s = "()(())((()()))"
Output: 3
"""

s ="()(())((()()))"

def maxDepth(s):
    currunt_char = 0
    max_char = 0

    for ch in s:
        if ch == '(':
            currunt_char +=  1
            max_char = max(currunt_char,max_char)

        elif ch == ')':
            currunt_char -= 1

    return max_char

print(maxDepth(s))


    
