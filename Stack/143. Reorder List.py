class Solution(object):
    def reorderList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        
        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the list
        prev, curr = None, slow.next
        slow.next = None  # Cut the first half from the second half
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # Step 3: Merge the two halves alternatingly
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2
            
        return head
