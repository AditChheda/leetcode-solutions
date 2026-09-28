"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_val = prices[0]
        for n in prices[1:]:
            if n < min_val:
                min_val = n
            else:
                profit = max(profit, n - min_val)
        return profit

# Time Complexity: O(n), where n is the number of days (length of the prices array).

# Space Complexity: O(1), as we are using a constant amount of space regardless of the input size.