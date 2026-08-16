"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = dict()
        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)
        
        freq = [[] for i in range(len(nums)+1)]
        for key, count in hashMap.items():
            freq[count].append(key)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# Time Complexity: O(n), where n is the number of elements in the input array nums.
# We iterate through the input array nums to build the hash map, which takes O(n)
# We then iterate through the hash map to build the frequency list, which takes O(n) in the worst case.
# Finally, we iterate through the frequency list to build the result list, which takes O(n) in the worst case.

# Space Complexity: O(n), where n is the number of elements in the input array nums.
# We use a hash map to store the frequency of each element, which takes O(n) space.
# We also use a list of lists to store the elements grouped by their frequency, which takes O(n) space.