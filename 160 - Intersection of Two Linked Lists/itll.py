# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        ptr_A_start = headA
        ptr_B_start = headB
        switched_A = False
        switched_B = False
        
        while ptr_A_start is not None and ptr_B_start is not None:
            if ptr_A_start = ptr_B_start:
                return ptr_A_start
            else:
                ptr_A_start = ptr_A_start.next
                if ptr_A_start is None:
                    if not switched_A:
                        ptr_A_start = headB
                        switched_A = True
                    else:
                        return None
                    
                ptr_B_start = ptr_B_start.next
                if ptr_B_start is None:
                    if not switched_B: 
                        ptr_B_start = headA
                        switched_B = True
                    else:
                        return None
        return None
