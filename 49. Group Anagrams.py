"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams
        for s in strs:
            count = [0] * 26 # representation for 26 letters
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

# Time Complexity: O(n * k), where n is the number of strings in the input array strs, 
# and k is the maximum length of a string in strs.
# We iterate through each string in strs, and for each string, we count the frequency of its characters, 
# which takes O(k) time. Therefore, the overall time complexity is O(n * k).

# Space Complexity: O(n * k), where n is the number of strings in the input array strs,
# and k is the maximum length of a string in strs. In the worst case, if all strings are anagrams 
# of each other, we may need to store all n strings in the hash map, and each string can have a 
# maximum length of k. Therefore, the space complexity is O(n * k).