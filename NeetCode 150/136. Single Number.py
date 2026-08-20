"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # n xor 0 = n
        res = 0 
        for n in nums:
            res = n ^ res 
        return res

# Time Complexity: O(n), where n is the number of elements in the input array nums. 
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.