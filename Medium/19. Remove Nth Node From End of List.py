class Solution(object):
    def removeNthFromEnd(self, head, n):
        ListNode = None
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next

# Notes:
# - Use two pointers to maintain a fixed gap of 'n' to find the target node in one pass.
# - Initial setup: A dummy node pointing to head, with 'first' and 'second' pointers at dummy.
# - Advance 'first' pointer by n + 1 steps to create the required gap.
# - Move both pointers at the same speed until 'first' reaches the end (None).
# - 'second' now points to the node just before the one to be removed.
# - Using a dummy node safely handles the edge case where the head itself is removed.
#
# Example Walkthrough: list=[1,2], n=2
# 'first' moves 3 steps to None. 'second' stays at dummy.
# second.next (node 1) is removed, returning dummy.next (node 2).
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique        : Two Pointers
# Difficulty/Pattern: Fast/Slow Pointers