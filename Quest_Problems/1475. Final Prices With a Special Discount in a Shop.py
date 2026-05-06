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