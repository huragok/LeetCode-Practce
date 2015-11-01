package rnkg;

public class Solution {
	public static class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
	public ListNode reverseKGroup(ListNode head, int k) {
		ListNode ptrNext = head;
		ListNode ptr;
		ListNode anchor = new ListNode(0);
		ListNode ptrTailReversed = anchor;
		anchor.next = head;
		while (ptrNext != null) {
			ptr = ptrNext;
			
			// Step ptrNext up to k
			int count = 0;
			while (count < k && ptrNext != null) {
				ptrNext = ptrNext.next; count++;
			}
			if (count < k) { // The left over section is shorter than k, leave it as it is
				ptrTailReversed.next = ptr;
				return anchor.next;
			} else {
				// Reverse the k nodes starting form ptr
				ListNode ptrTailTmp = ptr;
				ListNode ptrNextTmp = ptr.next;
				ListNode ptr
				for (int i = 0; i < k; i++) {
					
				}
			}
		}
    }
}
