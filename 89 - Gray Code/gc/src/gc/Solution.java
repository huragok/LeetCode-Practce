package gc;
import java.util.List;
import java.util.ArrayList;

public class Solution {
	public List<Integer> grayCode(int n) {
		List<Integer> result = new ArrayList<Integer> ();
		if (n == 0) {
			result.add(0);
			return result;
		} else if (n == 1) {
			result.add(0); result.add(1);
		} else {
			List<Integer> resultPartial = grayCode(n - 1);
			result.addAll(resultPartial);
			int head = 1;
			for (int i = 0; i < n - 1; i++) head <<= 1;
			for (int i = resultPartial.size() - 1; i >= 0; i--) {
				result.add(head + resultPartial.get(i));
			}
		}
		return result;
    }
	 
	public static void main(String [] args) {
		int n = 3;
		System.out.println(new Solution().grayCode(n));
	}
}
