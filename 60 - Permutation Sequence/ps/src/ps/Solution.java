package ps;

import java.util.List;
import java.util.LinkedList;

public class Solution {
	public String getPermutation(int n, int k) {
		if (n == 0) {
			return "";
		}
        int [] fact = new int [n];
        fact[0] = 1;
        for (int i = 1; i < n; i++) {
        	fact[i] = (i + 1) * fact[i - 1];
        }
        
        List<Integer> nums = new LinkedList<Integer> ();
        for (int i = 0; i < n; i++) {
        	nums.add(i + 1);
        }
        
        String result = "";
        for (int i = 0; i < n - 1; i++) {
        	int idx = (k - 1) / fact[n - 2 - i];
        	result += Integer.toString(nums.get(idx));
        	nums.remove(idx);
        	k -= idx * fact[n - 2 - i];
        }
        result += Integer.toString(nums.get(0));
        return result;
    }
	
	public static void main(String [] args) {
		int n = 3;
		for (int k = 1; k <= 6; k++)
		{
			System.out.println(new Solution().getPermutation(n, k));
		}
	}
}
