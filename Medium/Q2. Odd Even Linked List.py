class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenHead

        return head

# Notes:
# - Group all odd-indexed nodes together followed by the even-indexed nodes.
# - Use two pointers `odd` and `even` to build the two lists simultaneously.
# - Keep a reference to the head of the even list (`evenHead`) to attach it to the end of the odd list later.
#
# Example Walkthrough: head=[1,2,3,4,5]
# odd=1, even=2 (evenHead=2).
# odd.next=3 (even.next). odd=3.
# even.next=4 (odd.next). even=4.
# ... Result: 1->3->5->2->4
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Two Pointers / Linked List
# Pattern         : Interweaving / List Partition