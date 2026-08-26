"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest = 0, 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            length = r - l + 1
            longest = max(longest, length)
            seen.add(s[r])
        return longest

# Time Complexity: O(n), where n is the length of the string. Each character is processed 
# at most twice (once added and once removed from the set).
# Space Complexity: O(min(n, m)), where n is the length of the string and m is the size of the character set. 
# In the worst case, we may need to store all characters in the set.