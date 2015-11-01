package mksl;

import java.util.Comparator;

public class ListNodeComparator implements Comparator<ListNode>{
    @Override
    public int compare(ListNode x, ListNode y)
    {
        // Assume neither string is null. Real code should
        // probably be more robust
        // You could also just return x.length() - y.length(),
        // which would be more efficient.
        if (x.val < y.val)
        {
            return -1;
        }
        if (x.val > y.val)
        {
            return 1;
        }
        return 0;
    }
}
