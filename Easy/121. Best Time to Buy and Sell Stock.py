class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        
        return max_profit

# Notes:
# - Track the minimum price seen so far while iterating through the prices.
# - For each price, calculate the profit if sold today (price - min_price).
# - Update the maximum profit if the current profit is higher.
# - This ensures we only buy before we sell and in a single pass.
#
# Example Walkthrough: prices=[7, 1, 5, 3, 6, 4]
# price=7: min_price=7, max_profit=0
# price=1: min_price=1, max_profit=0
# price=5: min_price=1, max_profit=max(0, 5-1=4)=4
# price=6: min_price=1, max_profit=max(4, 6-1=5)=5
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Greedy / One Pass
# Pattern         : Maximum Difference
