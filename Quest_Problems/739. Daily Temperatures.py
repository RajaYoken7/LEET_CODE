class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Stores indices
        
        for i in range(n):
            # While stack is not empty and current temp is warmer than the temp 
            # at the index on top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                # Calculate the distance between days
                answer[prev_index] = i - prev_index
            
            # Push the current index onto the stack
            stack.append(i)
            
        return answer