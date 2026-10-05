"""
You are given a string s consisting of lowercase characters and an integer k, 
You have to count all possible substrings that have exactly k distinct characters.

Input: s = "abc", k = 2
Output: 2
Explanation: Possible substrings are ["ab", "bc"]

Input: s = "aba", k = 2
Output: 3
Explanation: Possible substrings are ["ab", "ba", "aba"]

Input: s = "aa", k = 1
Output: 3
Explanation: Possible substrings are ["a", "a", "aa"]
Constraints:
"""

s = "abaaca"
k = 1

def countSubstr(s,k):
    def AtMost(s,k):
        count = 0
        start = 0
        end = 0
        freq = {}

        for end in range(len(s)):
            if s[end] not in freq:
                freq[s[end]] = 0

            freq[s[end]] += 1

            while len(freq) > k:
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                start += 1

            count += end - start + 1

        return count

    return AtMost(s,k) - AtMost(s,k-1)

print(countSubstr(s,k))