import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # 1. Convert all stones to negative to simulate a Max-Heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        
        # 2. Continue smashing while there is more than 1 stone
        while len(max_heap) > 1:
            # Pop the two heaviest stones (the smallest negative values)
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)
            
            # If they are not equal, push the difference back
            if first != second:
                heapq.heappush(max_heap, first - second)
                
        # 3. If a stone remains, return its positive value; else 0
        return -max_heap[0] if max_heap else 0

# Notes:
# - Use a Max-Heap to efficiently retrieve the two heaviest stones at any step.
# - Since Python only has a Min-Heap (`heapq`), we negate the stone weights to simulate a Max-Heap.
# - Repeatedly pop the top two elements, subtract their original values, and push the difference if they aren't equal.
#
# Example Walkthrough: stones=[2,7,4,1,8,1]
# heapify -> [-8,-7,-4,-2,-1,-1]
# pop 8, 7. diff=1. push -1.
# heap -> [-4,-2,-1,-1,-1] ...
#
# Time Complexity : O(N log N)
# Space Complexity: O(N) for heap
# Technique       : Priority Queue / Max-Heap
# Pattern         : Top K / Simulation