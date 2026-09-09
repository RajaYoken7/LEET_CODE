# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        # remove from beginning
        while head and head.val == val:
            head = head.next

        curr = head
         
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

# Notes:
# - First, remove target values from the head of the list until the head is valid or None.
# - Then, iterate through the remaining list using a `curr` pointer.
# - If `curr.next` has the target value, skip it by assigning `curr.next = curr.next.next`.
# - Otherwise, just advance `curr`.
#
# Example Walkthrough: head=[6,1,2,6], val=6
# Head is 6, advance head -> [1,2,6].
# curr=1, curr.next=2 (keep). curr=2, curr.next=6.
# curr.next.val == 6, so curr.next = curr.next.next (None).
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Linked List Traversal
# Pattern         : In-place Removal
              
