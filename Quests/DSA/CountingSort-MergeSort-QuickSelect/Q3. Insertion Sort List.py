class Solution(object):
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
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
