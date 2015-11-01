# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None:
            return True
            
        ptr = head
        length = 1 # length of the linked list
        while ptr.next is not None:
            ptr = ptr.next
            length += 1
            
        if length == 1:
            return True
            
        idx_mid = length - length / 2
        ptr = head # Move the ptr to the second half of the linked list
        idx = 0
        while idx < idx_mid:
            ptr = ptr.next
            idx += 1
            
        # Reverse the second half of the linked list
        
        head_mid = ptr
        ptr = head_mid.next
        head_mid.next = None
        while ptr is not None:
            tmp = ptr.next
            ptr.next = head_mid
            head_mid = ptr
            ptr = tmp
            
        # Compare the first and the second half
        ptr1 = head
        ptr2 = head_mid
        for idx in range(length / 2):
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return True
        
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 2, 1]
    anchor = ListNode(None)
    ptr = anchor
    for n in nums:
        ptr.next = ListNode(n)
        ptr = ptr.next
    head = anchor.next
    print(Solution().isPalindrome(head))
        
