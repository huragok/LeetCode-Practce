package ts2;

public class Solution {
	public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;
        int [] result = new int [] {0, 0};
        int ptrLeft = 0, ptrRight = n - 1;
        while (ptrRight > ptrLeft) {
        	int sum = numbers[ptrLeft] + numbers[ptrRight];
        	if (sum == target) {
        		result[0] = ptrLeft + 1; result[1] = ptrRight + 1;
        		break;
        	} else if (sum < target) {
        		ptrLeft++;
        	} else {
        		ptrRight--;
        	}
        }
        return result;
    }
}
