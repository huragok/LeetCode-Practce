package ts3;

import java.util.Map;
import java.util.HashMap;

public class TwoSum {
	Map<Integer, Integer> count = new HashMap<Integer, Integer> ();
    // Add the number to an internal data structure.
	public void add(int number) {
	    if (count.containsKey(number)) {
	    	count.put(number, count.get(number) + 1);
	    } else {
	    	count.put(number, 1);
	    }
	}

    // Find if there exists any pair of numbers which sum is equal to the value.
	public boolean find(int value) {
	    for (int num: count.keySet()) {
	    	int rest = value - num;
	    	if (rest != num ) {
	    		if (count.containsKey(rest)) return true;
	    	} else {
	    		if (count.get(num) > 1) return true;
	    	}
	    }
	    return false;
	}
}


// Your TwoSum object will be instantiated and called as such:
// TwoSum twoSum = new TwoSum();
// twoSum.add(number);
// twoSum.find(value);
