"""
Given an integer array nums, return true if any value appears at least twice in the array, and 
return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

# Time Complexity: O(n), where n is the length of the input array nums. We iterate through the array once, 
# and each lookup and insertion operation in a hash set takes O(1) time on average.

# Space Complexity: O(n), where n is the length of the input array nums. In the worst case, if all elements are distinct,
# we may need to store all n elements in the hash set.