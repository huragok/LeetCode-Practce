package rl;

public class Solution {
	public class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
	public ListNode rotateRight(ListNode head, int k) {

        ListNode ptr = head;
        int n = 0;
        while (ptr != null) {
        	ptr = ptr.next;
        	n++;
        }
        if (n == 0) {
        	return head;
        }
        
        k %= n;
        if (k == 0) {
			return head;
		}
        
        ListNode ptrTailRight = head;
        for (int i = 0; i < k; i++) {
        	ptrTailRight = ptrTailRight.next;
        }
        ListNode ptrTailLeft = head;
        while (ptrTailRight.next != null) {
        	ptrTailRight = ptrTailRight.next;
        	ptrTailLeft = ptrTailLeft.next;
        }
        
        ListNode ptrHeadLeft = head;
        head = ptrTailLeft.next;
        ptrTailLeft.next = null;
        ptrTailRight.next = ptrHeadLeft;
        
        return head;
        
        
    }
}
