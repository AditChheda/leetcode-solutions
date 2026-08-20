"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.extend([nums[i], nums[i+n]])
        return ans

# Time Complexity: O(n), where n is the input integer. We iterate through the range from 0 to n once.
# Space Complexity: O(n), as we are storing the result in an array of length 2n.