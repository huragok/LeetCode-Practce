# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
            
        anchor = ListNode(None)
        ptr_unique = anchor
        ptr_probe = head
        val_current = head.val
        flag_unique = True
        while ptr_probe.next is not None:
            ptr_next = ptr_probe.next
            if ptr_next.val == val_current:
                flag_unique = False
            else: # Encounter a new value
                if flag_unique:
                    ptr_unique.next = ptr_probe
                    ptr_unique = ptr_unique.next
                    
                flag_unique = True
                val_current = ptr_next.val
            ptr_probe = ptr_next
            
        if flag_unique:
            ptr_unique.next = ptr_probe
            ptr_unique = ptr_unique.next
            ptr_unique.next = None
        else:
            ptr_unique.next = None
            
        return anchor.next
        
if __name__ == "__main__":
    nums = [1, 2, 2, 2]
    anchor = ListNode(None)
    ptr = anchor
    for n in nums:
        ptr.next = ListNode(n)
        ptr = ptr.next
    
    unique = Solution().deleteDuplicates(anchor.next)
    
    ptr = unique
    while ptr is not None:
        print(ptr.val)
        ptr = ptr.next
