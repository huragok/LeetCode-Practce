package sp;

import java.util.Arrays;
import java.util.List;
import java.util.LinkedList;

public class Solution {
	public String simplifyPath(String path) {
		String[] pathArray = path.split("/");;
		//System.out.println(Arrays.toString(pathArray));
		//return "";
		List<String> pathArraySimp = new LinkedList<String> ();
		for (String s: pathArray) {
			if (s.equals("") || s.equals(".")) {
				continue;
			} else if (s.equals("..")) {
				if (!pathArraySimp.isEmpty()) {
					pathArraySimp.remove(pathArraySimp.size() - 1);
				}
			} else {
				pathArraySimp.add(s);
			}
		}
		String result = "";
		if (pathArraySimp.isEmpty()) {
			return "/";
		}
		for (String s: pathArraySimp) {
			result += "/" + s;
		}
		return result;
    }
	
	public static void main(String [] args) {
		String path = "/home//foo/";
		System.out.println(new Solution().simplifyPath(path));
	}
}
