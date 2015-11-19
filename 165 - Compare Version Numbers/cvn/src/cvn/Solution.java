package cvn;

import java.util.Arrays;

public class Solution {
	public int compareVersion(String version1, String version2) {
		
		String [] v1, v2;
		if (version1.contains(".")) {
			System.out.println("fuck");
			v1 = version1.split("\\.");
		} else {
			v1 = new String [] {version1};
		}
		if (version2.contains(".")) {
			v2 = version2.split("\\.");
		} else {
			v2 = new String [] {version2};
		}
		System.out.println(Arrays.toString(v1));
		System.out.println(Arrays.toString(v2));
        int m = v1.length, n = v2.length;
        int reversed = 1;
        if (m > n) {
        	String [] vTmp = v1; v1 = v2; v2 = vTmp;
        	int tmp = m; m = n; n = tmp;
        	reversed = -1;
        }
        
        
        for (int i = 0; i < m; i++) {
        	int n1 = Integer.parseInt(v1[i]), n2 = Integer.parseInt(v2[i]);
        	if (n1 < n2) {
        		return -reversed;
        	} else if (n2 < n1) {
        		return reversed;
        	}
        }
        if (n > m) {
        	for (int i = m; i < n; i++) {
        		if (Integer.parseInt(v2[i]) > 0) {
        			return -reversed;
        		}
        	}
        	return 0;
        } else {
        	return 0;
        }
    }
	
	public static void main(String [] args) {
		String version1 = "1", version2 = "1.1";
		System.out.println(new Solution().compareVersion(version1, version2));
	}
}
