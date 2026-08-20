"""
LINK: https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
[Easy]
Kth Largest Element in a Stream
You are part of a university admissions office and need to keep track of the kth 
highest test score from applicants in real-time. This helps to determine cut-off 
marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a 
stream of test scores and continuously returns the kth highest test score after 
a new score has been submitted. More specifically, we are looking for the kth 
highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and 
the stream of test scores nums. int add(int val) Adds a new test score val to the stream and returns the 
element representing the kth largest element in the pool of test scores so far.
"""

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        # Convert the list into a min-heap
        heapq.heapify(self.nums)

        # Keep only the k largest elements in the heap
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # Add the new value to the heap
        heapq.heappush(self.nums, val)

        # If heap size exceeds k, remove the smallest element
        # so that only the k largest elements remain
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        # The smallest element in the heap is the kth largest overall
        return self.nums[0]

"""
Approach:
-Use a min-heap to store only the k largest elements seen so far.
-The smallest element in this heap is always the kth largest element in the stream.

During initialization:
-Build a heap from nums.
-Remove extra elements until the heap size becomes k.

During each add(val):
-Push val into the heap.
-If heap size becomes larger than k, pop the smallest element.
-Return the heap root.

Time Complexity:
Constructor: O(n log n) in the worst case because of heapify and possible removals.
add(val): O(log k) because heap operations are performed on a heap of size at most k.

Space Complexity:
O(k), since the heap stores at most k elements.
"""