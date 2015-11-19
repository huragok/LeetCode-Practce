package ms;

import java.util.Stack;

public class MinStack {
	
	private Stack<Integer> stack = new Stack<Integer> ();
	private Stack<Integer> stackMin = new Stack<Integer> ();
	
	public void push(int x) {
        stack.push(x);
        if (!stackMin.isEmpty() && stackMin.peek() < x) {
        	stackMin.push(stackMin.peek());
        } else {
        	stackMin.push(x);
        }
        return;
    }

    public void pop() {
        stackMin.pop();
        stack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return stackMin.peek();
    }
}
