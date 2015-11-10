package t;
import java.util.List;

public class Solution {
	
	public int minimumTotal(List<List<Integer>> triangle) {
		int n = triangle.size();
		int [] minSum = new int [n];
		for (int i = 0; i < n; i++) minSum[i] = triangle.get(n - 1).get(i);
		
		for (int j = n - 2; j >= 0; j--) {
			for (int i = 0; i <= j; i++) {
				minSum[i] = (minSum[i] > minSum[i + 1] ? minSum[i + 1] : minSum[i]) + triangle.get(j).get(i);
			}
		}
		return minSum[0];
    }
	
}
