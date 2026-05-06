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