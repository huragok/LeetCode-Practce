package vp;

import java.util.*;

public class Solution {
	public boolean isValid(String s) {
    	List<Character> stack = new ArrayList<Character> ();
    	Map<Character, Character> right2left = new HashMap<Character, Character> ();
    	right2left.put(')', '('); right2left.put(']', '['); right2left.put('}', '{');
        for (int i = 0; i < s.length(); i++) {
        	char c = s.charAt(i);
        	if (!right2left.containsKey(c)) { // A left parenthesis, push
        		stack.add(c);
        	} else {
        		if (stack.isEmpty() || stack.get(stack.size() - 1) != right2left.get(c)) {
        			return false;
        		} else {
        			stack.remove(stack.size() - 1);
        		}
        	}
        }
        return stack.isEmpty();
    }
	
	public static void main(String [] args) {
		String s = "([)]{}";
		System.out.println(new Solution().isValid(s));
	}
}