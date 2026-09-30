"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
"""

strs  = ["flower","flow","flight"]

def longestCommonPrefix(strs):

    result = ""
    first = strs[0]
    last = strs[-1]

    strs.sort()
    # strs  = ["flight","flow","flower"] after sort


    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return result

        result += first[i]


print(longestCommonPrefix(strs))