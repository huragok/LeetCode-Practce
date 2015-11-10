package pt2;

import java.util.List;
import java.util.ArrayList;

public class Solution {
	public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<Integer> ();
        if (rowIndex < 0) return row;
        row.add(1);
        for (int i = 1; i <= rowIndex; i++) {
        	for (int col = row.size() - 1; col >= 1; col--) row.set(col, row.get(col) + row.get(col - 1));
        	row.add(1);
        }
        return row;
    }
	
	public static void main(String [] args) {
		int rowIndex = 2;
		System.out.println(new Solution().getRow(rowIndex));
	}
}
