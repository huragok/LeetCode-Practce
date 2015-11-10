package pt;

import java.util.List;
import java.util.ArrayList;

public class Solution {
	public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<List<Integer>> ();
        if (numRows == 0) return result;
        
        List<Integer> row = new ArrayList<Integer> (1);
        row.add(1);
        result.add(row);
        for (int i = 1; i < numRows; i++) {
        	List<Integer> rowNew = new ArrayList<Integer> (i + 1);
        	rowNew.add(1);
        	for (int col = 1; col < i; col++) {
        		rowNew.add(row.get(col - 1) + row.get(col));
        	}
        	rowNew.add(1);
        	row = rowNew;
        	result.add(row);
        }
        return result;
    }
	
	public static void main(String [] args) {
		int numRows = 6;
		System.out.println(new Solution().generate(numRows));
	}
}
