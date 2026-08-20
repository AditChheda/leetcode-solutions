"""
Given a positive integer n, write a function that returns the number of set bits in its 
binary representation (also known as the Hamming weight).
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if n % 2 == 1:
                res += 1
            n = n // 2
        return res

# Time Complexity: O(log n), where n is the input integer. The number of iterations in the while loop 
# is proportional to the number of bits in n, which is log n.
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res

# Time Complexity: O(log n), where n is the input integer. The number of iterations in the while loop 
# is proportional to the number of bits in n, which is log n.
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res

# Time Complexity: O(k), where k is the number of set bits in n. The while loop iterates k times,
# where k is the number of set bits in n.
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.