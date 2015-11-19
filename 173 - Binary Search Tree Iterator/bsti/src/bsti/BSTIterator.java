package bsti;

public class BSTIterator {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	private TreeNode curr;
	
	public BSTIterator(TreeNode root) {
		curr = root; // Get to the leftmost node using Morris Traversal
		while (curr != null) {
			if (curr.left == null) {
				break;
			} else{
				TreeNode pre = curr.left;
				while (pre.right != null) pre = pre.right;
				pre.right = curr;
				curr = curr.left;
			}
		}
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return curr != null;
    }

    /** @return the next smallest number */
    public int next() {
        int result = curr.val;
        
        curr = curr.right;
        while (curr != null) {
        	if (curr.left == null) {
        		break;
        	} else {
        		TreeNode pre = curr.left;
        		while (pre.right != null && pre.right != curr) pre = pre.right;
        		if (pre.right == null) {
        			pre.right = curr;
        			curr = curr.left;
        		} else {
        			pre.right = null;
        			break;
        		}
        	}
        }
        
        return result;
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */
