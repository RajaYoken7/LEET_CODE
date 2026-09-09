class Solution(object):
    def deleteDuplicates(self, head):
        temp = head
        while (temp and temp.next):
            if (temp.next.val == temp.val):
                temp.next = temp.next.next
                continue
            temp = temp.next
        return head

# Notes:
# - Since the list is sorted, duplicates are adjacent.
# - Iterate through the list. If `temp.val == temp.next.val`, skip the next node by setting `temp.next = temp.next.next`.
# - Otherwise, just advance `temp`.
#
# Example Walkthrough: head=[1,1,2]
# temp=1. temp.next is 1. Equal!
# temp.next = 2 -> List becomes [1,2].
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Linked List Traversal
# Pattern         : In-place Removal
