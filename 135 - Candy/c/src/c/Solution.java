package c;
import java.util.Arrays;
public class Solution {
	public int candy(int[] ratings) {
     
		int n = ratings.length;
		int [] countCandy = new int [n];
		
		// Everyone get at least a candy
		for (int i = 0; i < n; i++) {
			countCandy[i] = 1;
		}
		
		// If the childs on the right gets a higher rating it needs to get more candies
		for (int i = 1; i < n; i++) {
			if (ratings[i] > ratings[i - 1]) countCandy[i] = countCandy[i - 1] + 1;
		}
		
		// If the childs on the left gets a higher rating it also needs to get more candies
		for (int i = n - 1; i >= 1; i--) {
			if (ratings[i - 1] > ratings[i] && countCandy[i - 1] < countCandy[i] + 1) countCandy[i - 1] = countCandy[i] + 1;
		}
		System.out.println(Arrays.toString(countCandy));
		int sum = 0;
		for (int i = 0; i < n; i++) {
			sum += countCandy[i];
		}
		return sum;
    }
	
	public static void main(String [] args) {
		int [] ratings = {4,2,3,4,1};
		System.out.println(new Solution().candy(ratings));
	}
}
