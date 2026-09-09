class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0
        target_tickets = tickets[k]
        
        for i in range(len(tickets)):
            if i <= k:
                # People at or before index k will be seen at most 
                # target_tickets times.
                time += min(tickets[i], target_tickets)
            else:
                # People after index k will be seen at most 
                # (target_tickets - 1) times before the kth person finishes.
                time += min(tickets[i], target_tickets - 1)
                
        return time

# Notes:
# - We can calculate the exact time each person spends buying tickets without simulating the queue step-by-step.
# - For person `i` <= `k`, they buy at most `tickets[k]` times.
# - For person `i` > `k`, they buy at most `tickets[k] - 1` times because the process stops when person `k` finishes.
#
# Example Walkthrough: tickets=[2,3,2], k=2 (target=2)
# i=0: min(2, 2) = 2
# i=1: min(3, 2) = 2
# i=2: min(2, 2) = 2 (stops here)
# Total time = 2+2+2 = 6.
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Math / Observation
# Pattern         : Queue Simulation