package po;

public class Solution {
	public int[] plusOne(int[] digits) {
        int n = digits.length;
        int carryOn = 1;
        for (int i = n - 1; i >= 0; i--) {
        	int tmp = digits[i] + carryOn;
        	digits[i] = tmp % 10;
        	carryOn = tmp / 10;
        	if (carryOn == 0) {
        		return digits;
        	}
        }
        
        int [] digitsNew = new int [n + 1];
        for (int i = 1; i < n + 1; i++){
        	digitsNew[i] = digits[i - 1];
        }
        digitsNew[0] = carryOn;
        return digitsNew;
    }
}
