package erpn;

import java.util.Stack;
import java.util.Set;
import java.util.HashSet;

public class Solution {
	private static Set<String> operators ;
	static {
		operators = new HashSet<String> ();
		operators.add("+"); operators.add("-"); operators.add("*"); operators.add("/");
	}
	
	public int evalRPN(String[] tokens) {
		Stack<String> stack = new Stack<String> ();
		int n = tokens.length;
		if (n == 0) return 0;
		
		for (String token: tokens) {
			if (operators.contains(token)) {
				int operand2 = Integer.parseInt(stack.pop());
				int operand1 = Integer.parseInt(stack.pop());
				if (token.equals("+")) {
					stack.push(Integer.toString(operand1 + operand2));
				} else if (token.equals("-")) {
					stack.push(Integer.toString(operand1 - operand2));
				} else if (token.equals("*")) {
					stack.push(Integer.toString(operand1 * operand2));
				} else {
					stack.push(Integer.toString(operand1 / operand2));
				}
			} else {
				stack.push(token);
			}
		}
		return Integer.parseInt(stack.pop());
    }
}
