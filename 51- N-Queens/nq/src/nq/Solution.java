package nq;

import java.util.List;
import java.util.LinkedList;
import java.util.Set;
import java.util.HashSet;

public class Solution {
	
	Set<Integer> colsOccupied = new HashSet<Integer>();
	Set<Integer> diagLTOccupied = new HashSet<Integer>();
	Set<Integer> diagRTOccupied = new HashSet<Integer>();
	List<String> template = new LinkedList<String> ();
	
    public List<List<String>> solveNQueens(int n) {
        for (int i = 0; i < n; i++) {
            String row = "";
            for (int j = 0; j < i; j++) {
            	row += ".";
            }
            row += 'Q';
            for (int j = i + 1; j < n; j++) {
            	row += ".";
            }
        	template.add(row);
        }
        
        List<Integer> path = new LinkedList<Integer> ();
        
        
        List<List<String>> sol = new LinkedList<List<String>> ();
        solveNQueensPartial(path, sol);
        return sol;
    }
    
    private void solveNQueensPartial(List<Integer> path, List<List<String>> sol) {
    	int n = template.size();
    	int row = path.size();
    	if (row == n) {
    		genSol(path, sol);
    	} else {
    		for (int col = 0; col < n; col++) {
    			if (valid(row, col)) {
    				path.add(col);
    				colsOccupied.add(col);
    				diagLTOccupied.add(col - row);
    				diagRTOccupied.add(col + row);
    				solveNQueensPartial(path, sol);
    				diagRTOccupied.remove(col + row);
    				diagLTOccupied.remove(col - row);
    				colsOccupied.remove(col);
    				path.remove(path.size() - 1);
    			}
    		}
    	}
    }
    
    private void genSol(List<Integer> path, List<List<String>> sol) {
    	List<String> s = new LinkedList<String> ();
    	for (int i = 0; i < path.size(); i++) {
    		s.add(template.get(path.get(i)));
    	}
    	sol.add(s);
    }
    
    private boolean valid(int row, int col) {
    	return !colsOccupied.contains(col) && !diagLTOccupied.contains(col - row) && !diagRTOccupied.contains(col + row);
    }
    
    public static void main(String [] args) {
    	int n = 4;
    	System.out.println(new Solution().solveNQueens(n));
    }
}
