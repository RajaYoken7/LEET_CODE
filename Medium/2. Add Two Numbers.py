
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ListNode = None
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10

            curr.next = ListNode(total % 10)
            
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next

# Notes:
# - Use a dummy node to easily build the result linked list.
# - Iterate while there are nodes in either list or there's a leftover carry.
# - At each step, sum the values of the current nodes and the carry.
# - The new node gets `total % 10` and the new carry is `total // 10`.
# - Advance the pointers (l1, l2, curr) and repeat.
#
# Example Walkthrough: l1=[2], l2=[8]
# val1=2, val2=8, carry=0 -> total=10. carry=1, node=0.
# Next iteration: l1=None, l2=None, carry=1 -> total=1. carry=0, node=1.
# Result: [0, 1] (which represents 10).
#
# Time Complexity : O(max(N, M))
# Space Complexity: O(1) excluding output list
# Technique       : Math / Linked List Traversal
# Pattern         : Linked List Addition