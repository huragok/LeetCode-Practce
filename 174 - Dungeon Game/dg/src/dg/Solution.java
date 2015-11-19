package dg;

public class Solution {
	public int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length;
        int n = dungeon[0].length;
        
        // Initialization;
        int [] h = new int [n];
        h[n - 1] = dungeon[m - 1][n - 1] < 0 ? 1 - dungeon[m - 1][n - 1] : 1;
        for (int j = n - 2; j >= 0; j--) {
        	int hTmp = h[j + 1] - dungeon[m - 1][j];
        	h[j] = hTmp > 1 ? hTmp : 1;
        }
        
        // Ride my knight of bronze
        for (int i = m - 2; i >= 0; i--) {
        	int hTmp = h[n - 1] - dungeon[i][n - 1];
        	h[n - 1] = hTmp > 1 ? hTmp : 1;
        	
        	for (int j = n - 2; j >= 0; j--) {
            	int hLess = h[j] > h[j + 1] ? h[j + 1] : h[j];
            	hTmp = hLess - dungeon[i][j];
            	h[j] = hTmp > 1 ? hTmp : 1;
            }
        }
        return h[0];
    }
}
