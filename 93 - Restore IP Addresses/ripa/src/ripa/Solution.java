package ripa;
import java.util.List;
import java.util.ArrayList;
public class Solution {
	public List<String> restoreIpAddresses(String s) {
		List<String> result = new ArrayList<String> ();
		List<Integer> path = new ArrayList<Integer> (4);
		
		restoreIpAddressesSince(s, path, 0, 4, result);
		return result;
		
    }
	
	private void restoreIpAddressesSince(String s, List<Integer> path, int idx, int nSeg, List<String> result) {
		if (nSeg == 0) {
			if (idx == s.length()) {
				String addr = path.get(0) + "." + path.get(1) + "." + path.get(2) + "." + path.get(3);
				result.add(addr);
			}
		} else {
			if (idx < s.length()) {
				if (s.charAt(idx) == '0') {
					path.add(0);
					restoreIpAddressesSince(s, path, idx + 1, nSeg - 1, result);
					path.remove(path.size() - 1);
				} else {
					for (int i = 0; i < 3 && i < s.length() - idx; i++) {
						int num = Integer.valueOf(s.substring(idx, i + idx + 1));
						if (num < 256) {
							path.add(num);
							restoreIpAddressesSince(s, path, idx + i + 1, nSeg - 1, result);
							path.remove(path.size() - 1);
						}
					}
				}
			}
		}
		return;
	}
	
	public static void main(String [] args) {
		String s = "25525511135";
		System.out.println(new Solution().restoreIpAddresses(s));
	}
}
