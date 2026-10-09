"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""


def longestPalindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1 : right]

    if not s or len(s) == 1:
        return s

    longest = ""

    for i in range(len(s)):
        pal1 = expand_around_center(i,i)
        pal2 = expand_around_center(i,i+1)

        if len(pal1) > len(longest):
            longest = pal1

        if len(pal2) > len(longest):
            longest = pal2

    return longest


s = "babababb"
print(longestPalindrome(s))