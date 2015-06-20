#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        
        ptr_origin = head # The pointer to the current position in the input linked list
        anchor = ListNode(None) #
        ptr_return = anchor # The pointer to the current position in the linked list to be returned
        if head is None:
            return None
        while ptr_origin is not None:
            
            # Push k nodes in stack
            stack = list()
            for i_stack in range(k):
                stack.append(ptr_origin)
                #print("Pushing {0}".format(ptr_origin.val))
                ptr_origin = ptr_origin.next

                if ptr_origin is None:
                    break;
                    
            if len(stack) == k:
                # Pop them the stacked nodes to the returned linked list
                for i_stack in range(k - 1, -1, -1):
                    ptr_return.next = stack[i_stack]
                    #print("Poping {0}".format(stack[i_stack].val))
                    ptr_return = ptr_return.next
                    
                #ptr_return.next = stack[0]
                #print("Poping {0}".format(stack[0].val))
            else:
                for i_stack in range(len(stack)):
                    ptr_return.next = stack[i_stack]
                    ptr_return = ptr_return.next
            
        #ptr_return = ptr_return.next
        ptr_return.next = None
        return anchor.next
        
        
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    result = Solution().reverseKGroup(head, 1)
                
                
        
        
