"""
Given an array of positive integers nums and a positive integer target, return the 
minimal length of a subarray whose sum is greater than or equal to target. If there is 
no such subarray, return 0 instead.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_val = float("inf")
        l = 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_val = min(min_val, r - l + 1)
                total -= nums[l]
                l += 1
        return min_val if min_val < float("inf") else 0

# Time Complexity: O(n)
# Space Complexity: O(1)