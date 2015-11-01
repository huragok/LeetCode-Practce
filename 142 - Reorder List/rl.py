# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        # Corner cases
        if head is None or head.next is None or head.next.next is None:
            return
            
        # Locate the head of the second half of the linked list
        ptr_1x = head
        ptr_2x = head.next
        while ptr_2x is not None:
            if ptr_2x.next is None:
                break
            else:
                ptr_1x = ptr_1x.next
                ptr_2x = ptr_2x.next
                if ptr_2x.next is None:
                    break
                ptr_2x = ptr_2x.next
        mid = ptr_1x.next
        mid_prev = ptr_1x
        
        # Reverse the second half of the linked list
        mid_prev.next = None
        mid_new = self._reverse(mid)

        #return mid_new
        
        # Interleave two linked list, the first half goes first
        ptr1 = head
        ptr2 = mid_new
        while ptr1 is not None:
            ptr1_new = ptr1.next
            ptr2_new = None if ptr2 is None else ptr2.next
            
            ptr1.next = ptr2
            if ptr2 is not None:
                ptr2.next = ptr1_new
            
            ptr1 = ptr1_new
            ptr2 = ptr2_new
            
        return
            
        
    # Function to reverse the linked list
    def _reverse(self, head):
        stack = []
        ptr = head
        while ptr is not None:
            stack.append(ptr)
            ptr = ptr.next
            
        anchor = ListNode(None)
        ptr = anchor
        while stack:
            node = stack.pop(-1)
            ptr.next = node
            ptr = ptr.next
            
        ptr.next = None
        return anchor.next
        
    # print linked list
    def _print(self, head):
        s = ''
        ptr = head
        while ptr is not None:
            s += "{0}".format(ptr.val)
            s += ' -> '
            ptr = ptr.next
        s += 'None'
        print(s)
            
if __name__ == "__main__":
    nums = range(6)
    anchor = ListNode(None)
    ptr = anchor
    for n in nums:
        ptr.next = ListNode(n)
        ptr = ptr.next
        
    #(head_new, end_new) = Solution()._reverse(anchor.next)
    #Solution()._print(head_new)
    Solution().reorderList(anchor.next)
    Solution()._print(anchor.next)
