package ms;
import java.util.List;
import java.util.ArrayList;
public class Solution {
	public String multiply(String num1, String num2) {
		Num n1 = new Num(num1);
		Num n2 = new Num(num2);
		System.out.println(n1);
		System.out.println(n2);
        Num p = n1.multiply(n2);
        return p.toString();
    }
	
	class Num {
		private List<Integer> numList;
		
		public Num(String num) {
			numList = new ArrayList<Integer> (num.length());
			for (int i = num.length() - 1; i >= 0  ; i--) {
				numList.add(Character.getNumericValue(num.charAt(i)));
			}
		}
		
		public int length() {
			return numList.size();
		}
		
		public Num(List<Integer> numListOther) {
			numList = numListOther;
		}
		
		public Num multiply(Num other) {
			int m = this.length();
			int n = other.length();
			
			List<Integer> result = new ArrayList<Integer> (m + n);
			for (int i = 0; i < m + n; i++) {
				result.add(0);
			}
			
			List<List<Integer>> buffer = new ArrayList<List<Integer>> (m);
			for (int i = 0; i < m; i++) {
				List<Integer> bufferEntry = new ArrayList<Integer> (n + 1);
				for (int j = 0; j < n; j++) {
					bufferEntry.add(0);
				}
				for (int j = 0; j < n; j++) {
					int tmp = this.numList.get(i) * other.numList.get(j) + bufferEntry.get(j);
					int carryOn = tmp / 10;
					tmp %= 10;
					bufferEntry.set(j, tmp);
					bufferEntry.set(j + 1, bufferEntry.get(j + 1) + carryOn);
				}
			}
			
			for (int l = 0; l < m + n; l++) {
				result.set()
			}
			
			int l = m + n - 1;
			while (l >= 0) {
				if (result.get(l) > 0) {
					break;
				}
				l--;
			}
			return new Num(result.subList(0, l + 1));
		}
		
		public String toString() {
			String result = "";
			for (int i = this.length() - 1; i >=0; i--) {
				result += Integer.toString(numList.get(i));
			}
			return result;
		}
	}
	
	public static void main(String [] args) {
		String num1 = "13";
		String num2 = "124";
		System.out.println(new Solution().multiply(num1, num2));
	}
}
