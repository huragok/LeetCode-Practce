package nq2;

import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;

public class Solution {
	private Set<Integer> colsOccupied = new HashSet<Integer> ();
	private Set<Integer> diagLTOccupied = new HashSet<Integer> ();
	private Set<Integer> diagRTOccupied = new HashSet<Integer> ();
	int result;
	int n;
	
	public int totalNQueens(int n) {
		result = 0;
		this.n = n;
        List<Integer> path = new ArrayList<Integer> (n);
        helper(path);
        return result;
    }
	
	private void helper(List<Integer> path) {
		int row = path.size();
		if (row == n) {
			result += 1;
		} else {
			for (int col = 0; col < n; col++) {
				if (valid(row, col)) {
					path.add(col);
					colsOccupied.add(col);
					diagLTOccupied.add(col - row);
					diagRTOccupied.add(col + row);
					helper(path);
					path.remove(path.size() - 1);
					colsOccupied.remove(col);
					diagLTOccupied.remove(col - row);
					diagRTOccupied.remove(col + row);
				}
			}
		}
		
	}
	
	private boolean valid(int row, int col) {
		return !colsOccupied.contains(col) && !diagLTOccupied.contains(col - row) && !diagRTOccupied.contains(col + row);
	}
	
	public static void main(String [] args) {
		int n = 4;
		System.out.println(new Solution().totalNQueens(n));
	}
}
