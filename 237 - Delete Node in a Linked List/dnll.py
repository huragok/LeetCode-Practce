# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        ptr = node
        ptr_prev = None
        while ptr.next is not None:
            ptr_prev = ptr
            ptr.val = ptr.next.val
            ptr = ptr.next
            
        ptr_prev.next = None
