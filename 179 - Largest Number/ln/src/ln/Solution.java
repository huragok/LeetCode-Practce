package ln;
import java.util.Comparator;
import java.util.Arrays;

public class Solution {
	public class ConcatComparator implements Comparator<Integer> {
		public int compare(Integer x, Integer y) {
			String xy = Integer.toString(x) + Integer.toString(y);
			String yx = Integer.toString(y) + Integer.toString(x);
			return xy.compareTo(yx);
		}
	};
	
	public String largestNumber(int[] nums) {
		Integer [] numsObj = new Integer [nums.length];
		for (int i = 0; i < nums.length; i++) numsObj[i] = nums[i];
        Arrays.sort(numsObj, new ConcatComparator());
        if (numsObj[numsObj.length - 1] == 0) return "0";
        
        StringBuilder result = new StringBuilder();
        for (int num: numsObj) {
        	result.insert(0, Integer.toString(num));
        }
        
        return result.toString();
    }
}
