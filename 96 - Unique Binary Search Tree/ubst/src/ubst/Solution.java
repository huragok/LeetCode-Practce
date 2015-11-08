package ubst;

public class Solution {
	public int numTrees(int n) {
		int [][] countTrees = new int [n + 1][n + 1]; // countTrees[i][d] is the number of trees from [i, i+d)
		
		for (int i = 0; i <= n; i++){
			countTrees[i][0] = 1;
		}
		
		for (int d = 1; d <= n; d++) {
			for (int i = 0; i <= n - d; i++) {
				countTrees[i][d] = 0;
				for (int valRoot = i; valRoot < i + d; valRoot++) {
					countTrees[i][d] += countTrees[i][valRoot - i] * countTrees[valRoot + 1][i + d - valRoot - 1];
				}
			}
		}
        return countTrees[0][n];
    }
}
