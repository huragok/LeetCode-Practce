package clrp;

import java.util.Map;
import java.util.HashMap;

public class Solution {
	static class RandomListNode {
		int label;
		RandomListNode next, random;
		RandomListNode(int x) { this.label = x; }
	};
	
	public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) return null;
        RandomListNode headNew = new RandomListNode (head.label);
        RandomListNode ptr = head, ptrNew = headNew;
        Map<Integer, RandomListNode> nodesNew = new HashMap<Integer, RandomListNode> ();
        nodesNew.put(headNew.label, headNew);
        while (ptr.next != null) {
        	ptr = ptr.next;
        	RandomListNode nodeNew = new RandomListNode (ptr.label);
        	ptrNew.next = nodeNew;
        	ptrNew = ptrNew.next;
        	
        	nodesNew.put(nodeNew.label, nodeNew);
        }
        ptrNew.next = null;
        
        ptr = head; ptrNew = headNew;
        while (ptr != null) {
        	if (ptr.random != null) {
        		ptrNew.random = nodesNew.get(ptr.random);
        		
        	}
        	ptr = ptr.next;
    		ptrNew = ptrNew.next;
        }
        
        return headNew;
    }
	
	public static void main (String [] args) {
		
	}
}
