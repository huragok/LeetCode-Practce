# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        else:
            #split the list into two
            ptr_1x = head
            ptr_2x = head.next
            while ptr_2x.next is not None:
                ptr_1x = ptr_1x.next
                ptr_2x = ptr_2x.next
                if ptr_2x.next is None:
                    break
                else:
                    ptr_2x = ptr_2x.next
            head1 = head
            head2 = ptr_1x.next
            ptr_1x.next = None
            
            
            head1 = self.sortList(head1)
            head2 = self.sortList(head2)
            head = self._mergeList(head1, head2)
            return head
        
        
    def _mergeList(self, head1, head2):
        anchor = ListNode(None)
        ptr1 = head1
        ptr2 = head2
        ptr_sorted = anchor
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val > ptr2.val:
                ptr_sorted.next = ptr2
                ptr2 = ptr2.next
            else:
                ptr_sorted.next = ptr1
                ptr1 = ptr1.next
            ptr_sorted = ptr_sorted.next
        if ptr1 is None:
            ptr_sorted.next = ptr2
        else:
            ptr_sorted.next = ptr1
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
    nums = [1, 3, 2,5,4]
    anchor = ListNode(None)
    ptr = anchor
    for n in nums:
        ptr.next = ListNode(n)
        ptr = ptr.next
        
    head = Solution().sortList(anchor.next)
    Solution()._print(head)
