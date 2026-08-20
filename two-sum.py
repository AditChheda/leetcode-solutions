"""
LINK: https://leetcode.com/problems/two-sum/description/
[Easy]
Two Sum 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Stores previously seen numbers and their indices.
        # Key   -> number
        # Value -> index
        seen = {}

        # Iterate through the array once.
        for i in range(len(nums)):
            # Compute the value needed to reach the target.
            complement = target - nums[i]

            # If the complement has already been seen, we've found the pair.
            if complement in seen:
                return [seen[complement], i]

            # Store the current number for future lookups.
            seen[nums[i]] = i

"""
Approach:
- Use a hash map to store previously visited numbers.
- For each element, check whether its complement exists in the hash map.
- If found, return the stored index and the current index.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Check every possible pair in the array.
        for i in range(len(nums)):
            # Determine the value needed to reach the target.
            complement = target - nums[i]

            # Search the remaining elements for the complement.
            for j in range(i + 1, len(nums)):
                if nums[j] == complement:
                    return [i, j]

"""
Approach:
- Compare each element with every element that comes after it.
- Return the indices as soon as a valid pair is found.

Time Complexity: O(n²)
Space Complexity: O(1)
"""
