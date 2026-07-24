class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Notes:
# - Floyd's Cycle-Finding Algorithm (Tortoise and Hare).
# - Use two pointers, `slow` moving one step and `fast` moving two steps.
# - If there is a cycle, the `fast` pointer will eventually catch up to the `slow` pointer inside the cycle.
# - If `fast` reaches `None`, there is no cycle.
#
# Example Walkthrough: 1 -> 2 -> 3 -> 4 -> 2...
# s=1, f=1
# s=2, f=3
# s=3, f=2
# s=4, f=4 (match, cycle exists).
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Two Pointers / Fast & Slow Pointers
# Pattern         : Cycle Detection
