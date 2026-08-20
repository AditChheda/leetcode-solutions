"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = dict(), dict()
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True 

# Time Complexity: O(n), where n is the length of the input strings s and t. 
# We iterate through both strings once to build the frequency counts, and then we 
# iterate through the keys of countS to compare the counts.

# Space Complexity: O(1), since the size of the hash maps countS and countT is bounded 
# by the number of unique characters in the input strings, which is at most 26 for lowercase 
# English letters. Therefore, the space used by the hash maps does not scale with the input size.