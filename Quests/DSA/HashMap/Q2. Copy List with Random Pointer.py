class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        temp = head
        while temp:
            newNode = Node(temp.val)
            newNode.next = temp.next
            temp.next = newNode
            temp = newNode.next
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        temp = head
        copyHead = head.next
        copyTemp = copyHead
        while temp:
            temp.next = temp.next.next
            if copyTemp.next:
                copyTemp.next = copyTemp.next.next
            temp = temp.next
            copyTemp = copyTemp.next
        return copyHead