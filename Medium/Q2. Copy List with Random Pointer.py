class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        temp = head
        while temp:
            Node = None
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

# Notes:
# - Create deep copy of linked list with random pointers in O(N) time.
# - Phase 1: Weave copied nodes into the original list: A -> A' -> B -> B'...
#    This preserves the original list structure while adding copies.
# - Phase 2: Assign random pointers for copied nodes:
#    If A.random = B, then A'.random = B' (which is B.next).
# - Phase 3: Separate the copied list from the original list.
# - Use dummy nodes to simplify edge cases (empty list, single node, etc.).
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Interweaving / In-place modification
# Pattern         : Deep Copy with Additional Pointers
