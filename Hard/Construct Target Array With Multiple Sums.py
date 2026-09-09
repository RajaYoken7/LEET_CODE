import heapq

class Solution:
    def isPossible(self, target: list[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        
        total_sum = sum(target)
        # 1. Create a Max-Heap (using negative values for Python's heapq)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)
        
        while True:
            # 2. Get the current largest element
            largest = -heapq.heappop(max_heap)
            rest_sum = total_sum - largest
            
            # 3. Base case: if largest is 1, we successfully reverted all to 1s
            if largest == 1 or rest_sum == 1:
                return True
            
            # 4. Check for impossible scenarios
            # rest_sum == 0 happens if target has only one element (handled above)
            # largest < rest_sum means it couldn't have been the sum of others
            if rest_sum == 0 or largest <= rest_sum:
                return False
            
            # 5. Calculate the previous value using modulo for efficiency
            # This handles cases where one number is much larger than the sum of others
            prev_val = largest % rest_sum
            
            # If modulo is 0, the previous value must have been rest_sum itself
            # But if rest_sum is not 1, we can't reach 1, so it's impossible
            if prev_val == 0:
                return False
            
            # 6. Update total sum and push the new value back into heap
            total_sum = rest_sum + prev_val
            heapq.heappush(max_heap, -prev_val)

# Notes:
# - Work backwards from the target array to [1, 1, ..., 1] using a Max-Heap.
# - The largest element was formed by adding the rest of the array sum to some previous value.
# - `prev_val = largest % rest_sum` is used to handle large jumps quickly.
# - If we can reduce the largest element to a valid previous state, we push it back.
#
# Example Walkthrough: target=[9,3,5]
# sum=17. heap=[-9,-5,-3]. pop 9.
# rest_sum=17-9=8. prev = 9 % 8 = 1.
# push 1. heap=[-5,-3,-1]. total_sum=8+1=9...
#
# Time Complexity : O(N log N)
# Space Complexity: O(N) for heap
# Technique       : Priority Queue / Max-Heap
# Pattern         : Working Backwards