class Solution(object):
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        ListNode = None
        dummy = ListNode(-float('inf'))
        dummy.next = head
        cur = head
        while cur and cur.next:
            if cur.next.val >= cur.val:
                cur = cur.next
            else:
                temp = cur.next
                cur.next = temp.next
                pre = dummy
                while pre.next.val < temp.val:
                    pre = pre.next
                temp.next = pre.next
                pre.next = temp
        return dummy.next

# Notes:
# - Use a dummy node to act as the head of the sorted portion.
# - Iterate through the list with `cur`.
# - If `cur` is already in order (`cur.next.val >= cur.val`), just advance `cur`.
# - Otherwise, remove `cur.next` (temp) and insert it into the correct position in the sorted portion starting from `dummy`.
#
# Example Walkthrough: head=[4,2,1,3]
# dummy->4->2->... cur=4. temp=2. 2 < 4.
# remove 2. search from dummy. insert 2 after dummy. dummy->2->4->...
#
# Time Complexity : O(N^2)
# Space Complexity: O(1)
# Technique       : Linked List Traversal
# Pattern         : Insertion Sort
