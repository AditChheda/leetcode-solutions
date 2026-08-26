"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        nums_cur = max_cur = sum(nums[:k])
        for i in range(len(nums)-k):
            nums_cur += nums[k+i] - nums[i]
            max_cur = max(max_cur,nums_cur)
        return max_cur/k  


# Time Complexity: O(n), where n is the length of the input array nums. We iterate through 
# the array once to calculate the maximum average.
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.