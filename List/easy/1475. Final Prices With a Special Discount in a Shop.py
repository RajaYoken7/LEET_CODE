class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = [] # Stores indices of prices
        
        for i in range(len(prices)):
            # While the stack is not empty and the current price
            # is less than or equal to the price at the index on top of the stack
            while stack and prices[stack[-1]] >= prices[i]:
                # We found the discount for the item at index stack.pop()
                last_index = stack.pop()
                prices[last_index] -= prices[i]
            
            # Push current index onto the stack to find its discount later
            stack.append(i)
            
        return prices

# Notes:
# - Use a Monotonic Stack to find the next smaller or equal element for each item.
# - The stack stores indices of items waiting for a discount.
# - For each price, pop items from the stack if the current price is a valid discount (<= stacked item).
# - Apply the discount and push the current index to find its discount later.
#
# Example Walkthrough: prices=[8,4,6]
# i=0, price=8: stack=[0]
# i=1, price=4: 4 <= 8. Pop 0, prices[0] -= 4 -> 4. stack=[1]
# i=2, price=6: 6 > 4. No discount for stack top. stack=[1,2]
#
# Time Complexity : O(N)
# Space Complexity: O(N) for stack
# Technique       : Monotonic Stack
# Pattern         : Next Greater/Smaller Element