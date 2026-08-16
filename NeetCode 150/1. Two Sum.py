"""
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict() # value : index
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in hashMap:
                return [hashMap[diff], idx]
            hashMap[val] = idx

# Time Complexity: O(n), where n is the length of the input array nums. 
# We iterate through the array once, and each lookup and insertion operation in a hash map takes O(1) time on average.

# Space Complexity: O(n), where n is the length of the input array nums.
# In the worst case, if all elements are distinct, we may need to store all n elements in the hash map.