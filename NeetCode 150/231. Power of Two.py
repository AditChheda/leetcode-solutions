"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0  and n & (n - 1) == 0 # a positive power of 2 has exactly one 1 bit.

# Time Complexity: O(1), as we are performing a constant number of operations regardless of the input size.
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.
