package up2;

public class Solution {
	public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        if (m == 0) return 0;
        int n = obstacleGrid[0].length;
        if (n == 0) return 0;
        
        int [] count = new int [n];
        count[0] = obstacleGrid[0][0] == 0 ? 1 : 0;
        for (int col = 1; col < n; col++) {
        	count[col] = count[col - 1] & (1 - obstacleGrid[0][col]);
        }
        
        for (int row = 1; row < m; row++) {
        	count[0] = count[0] & (1 - obstacleGrid[row][0]);
        	for (int col = 1; col < n; col++) {
        		if (obstacleGrid[row][col] == 0) {
        			count[col] += count[col - 1];
        		} else {
        			count[col] = 0;
        		}
        	}
        }
        return count[n - 1];
    }
	
	public static void main(String [] args) {
		int [][] obstacleGrid = new int [3][3];
		obstacleGrid[0] = new int [] {0, 0, 0};
		obstacleGrid[1] = new int [] {0, 1, 0};
		obstacleGrid[2] = new int [] {0, 0, 0};
		System.out.println(new Solution().uniquePathsWithObstacles(obstacleGrid));
	}
}
