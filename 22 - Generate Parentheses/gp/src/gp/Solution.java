package gp;

import java.util.*;

public class Solution {
	public List<String> generateParenthesis(int n) {
        if (n == 1) {
        	return Arrays.asList("()");
        } else {
        	Set<String> parenthesis = new HashSet<String> ();
        	
        	List<String> parenthesisPartial = generateParenthesis(n - 1);
        	for (String s: parenthesisPartial) {
        		parenthesis.add("(" + s + ")");
        	}
        	
        	for (int left = 1; left <= n / 2; left++) {
        		List<String> parenthesisPartialLeft = generateParenthesis(left);
        		List<String> parenthesisPartialRight = generateParenthesis(n - left);
        		for (String sl: parenthesisPartialLeft) {
        			for (String sr: parenthesisPartialRight) {
        				parenthesis.add(sl + sr);
        				parenthesis.add(sr + sl);
        			}	
            	}
        	}
        	
        	List<String> result = new ArrayList<String> (parenthesis.size());
        	result.addAll(parenthesis);
        	return result;
        }
    }
	
	public static void main(String [] args) {
		int n = 4;
		System.out.println(new Solution().generateParenthesis(n));
	}
}
