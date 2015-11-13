package lruc;

import java.util.Map;
import java.util.HashMap;

public class LRUCache {
    public static class ListNode{
    	int key, val;
    	ListNode next, prev;
    	ListNode (int k, int v) {key = k; val = v; next = null; prev = null;};
    };
    
    private int cap;
	private ListNode head, tail;
	private Map<Integer, ListNode> map;
	
    public LRUCache(int capacity) {
    	cap = capacity;
    	head = new ListNode(0, 0); tail = new ListNode(0, 0);
    	head.next = tail; tail.prev = head;
    	map = new HashMap<Integer, ListNode> ();
    }
    
    public int get(int key) {
        if (!map.containsKey(key)) return -1;
        ListNode node = map.get(key);
        remove(node);
        add(node);
        return node.val;
    }
    
    public void set(int key, int value) {
        if (map.containsKey(key)) {
        	ListNode node = map.get(key);
        	remove(node);
        	node.val = value;
        	add(node);
        } else {
        	if (map.size() == cap) {
        		ListNode nodeToRemove = head.next;
        		remove(nodeToRemove);
        		map.remove(nodeToRemove.key);	
        	}
        	
        	ListNode node = new ListNode(key, value);
        	map.put(key, node);
        	add(node);
        }
    }
    
    private void add(ListNode node) {
    	tail.prev.next = node;
    	node.prev = tail.prev;
    	node.next = tail;
    	tail.prev = node;
    	return;
    }
    
    private void remove(ListNode node) {
    	node.prev.next = node.next;
    	node.next.prev = node.prev;
    	return;
    }
}