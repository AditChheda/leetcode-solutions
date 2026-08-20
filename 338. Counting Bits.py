"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Do not solve it with built-in functions (i.e., like __builtin_popcount in C++).
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            count = 0
            while i:
                i = i & (i - 1)
                count += 1
            ans.append(count)
        return ans

# Time Complexity: O(n * k), where n is the input integer and k is the number of set bits in each integer from 0 to n.
# Space Complexity: O(n), as we are storing the result in an array of length n + 1.

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i & (i - 1)] + 1
        return ans

# Time Complexity: O(n), where n is the input integer. We iterate through the range from 1 to n once.
# Space Complexity: O(n), as we are storing the result in an array of length n + 1.