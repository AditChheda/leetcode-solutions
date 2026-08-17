"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in hashSet:
                length = 1
                while (n + length) in hashSet:
                    hashSet.remove(n + length)
                    length += 1
                longest = max(longest, length)
        return longest

# Time Complexity: O(n)
# Space Complexity: O(n)
