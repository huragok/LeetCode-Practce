# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
            
        head_new = RandomListNode(head.label)
        ptr = head
        ptr_new = head_new
        node_set = {None: None, head.label: head_new}
        
        while ptr.next is not None:
            ptr = ptr.next
            node_new = RandomListNode(ptr.label)
            ptr_new.next = node_new
            ptr_new = ptr_new.next
            node_set[ptr.label] = node_new
            
        ptr = head
        ptr_new = head_new
        while ptr is not None:
            ptr_new.random = None if ptr.random is None else node_set[ptr.random.label]
            ptr = ptr.next
            ptr_new = ptr_new.next
            
        return head_new
            
        
