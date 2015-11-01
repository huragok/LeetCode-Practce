# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
            
        anchor = ListNode(None)
        anchor.next = head
        
        # Detect the boundary of the range to be reversed and the node before and after the boundary
        ptr_probe = head
        ptr_probe_prev = anchor
        
        count = 1
        while count < n:
            if count == m:
                ptr_before = ptr_probe_prev
                ptr_left = ptr_probe
            ptr_probe_prev = ptr_probe
            ptr_probe = ptr_probe.next
            count += 1

            
        ptr_right = ptr_probe
        ptr_after = ptr_probe.next
        # print(ptr_before.val, ptr_left.val, ptr_right.val, ptr_after.val)
        
        # Start the reversion
        for idx in range(n - m):
            ptr_next = ptr_left.next
            ptr_left.next = ptr_after
            ptr_right.next = ptr_left
            ptr_after = ptr_left
            ptr_left = ptr_next
            
        ptr_before.next = ptr_left
        
        return anchor.next
        
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    m = 2
    n = 4
    
    anchor = ListNode(None)
    ptr = anchor
    for num in nums:
        ptr.next = ListNode(num)
        ptr = ptr.next

    head = Solution().reverseBetween(anchor.next, m, n)
    
    ptr = head
    while ptr is not None:
        print(ptr.val)
        ptr = ptr.next
         
