class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        prev = None
        curr = head
        while curr:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        return prev

# Notes:
# - Iterate through the list, changing the `next` pointer of each node to point to the previous node.
# - Maintain a `prev` pointer (initially None) and a `curr` pointer (initially head).
# - Temporarily store `curr.next` before overwriting it so we don't lose the rest of the list.
# - Return `prev` as the new head once `curr` reaches the end.
#
# Example Walkthrough: head=[1,2,3]
# curr=1, prev=None. nextNode=2. 1.next=None. prev=1, curr=2.
# curr=2, prev=1. nextNode=3. 2.next=1. prev=2, curr=3.
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Linked List Traversal
# Pattern         : In-place Reversal