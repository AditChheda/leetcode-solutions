"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest, temp = 0, 0
        for n in nums:
            if n == 0:
                temp = 0
            else:
                temp += 1
                longest = max(longest, temp)
        return longest

# Time Complexity: O(n), where n is the length of the input array nums. We iterate through the array once.
# Space Complexity: O(1), as we are using a constant amount of space for the variables longest and temp.