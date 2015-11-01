# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
            return None
        elif head.next is None:
            return None
            
        ptr_1x = head
        ptr_2x = head.next
        while ptr_1x is not None and ptr_2x is not None:
            if ptr_1x == ptr_2x:
                break
            ptr_1x = ptr_1x.next
            ptr_2x = ptr_2x.next
            if ptr_2x is not None:
                ptr_2x = ptr_2x.next
            else:
                return None
        if ptr_2x is None:
            return None
            
        ptr_2x = ptr_2x.next
        ptr_1x = head
        while ptr_1x != ptr_2x:
            ptr_1x = ptr_1x.next
            ptr_2x = ptr_2x.next
            
        return ptr_1x
