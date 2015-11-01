# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        n = len(intervals) # Number of intervals
        if n == 0:
            return [newInterval]
        pos = self._bisect(intervals, newInterval)
        
        intervals.insert(pos, newInterval) # Insert the new interval
        for interval in intervals:
            print("[{0}, {1}], ".format(interval.start, interval.end))
        # Starting merge from pos - 1
        if pos == 0:
            result = self.merge(intervals, 0)
        else:
            result = self.merge(intervals, pos - 1)
            
        return result
        
    # Using bisect search to locate the position to insert the new interval
    def _bisect(self, intervals, newInterval):
        n = len(intervals) # Number of intervals
        # The left and right bound for the search 
        l = 0 
        r = n - 1
        
        if newInterval.start < intervals[0].start:
            return 0
        elif newInterval.start >= intervals[n - 1].start:
            return n
        
        while r - l  > 1:
            m = (l + r) / 2
            if newInterval.start < intervals[m].start:
                r = m
            else:
                l = m
        
        return l + 1
        
    # Starting to merge interval from intervals[start]
    def merge(self, intervals, start):
        n = len(intervals)
        if start == 0:
            result = []
        else:
            result = intervals[0 : start]
            
        interval_tmp = intervals[start]
        for i in range(start + 1, n):
            
            interval_new = intervals[i]
            print((interval_tmp.start, interval_tmp.end))
            print((interval_new.start, interval_new.end))
            if interval_new.start <= interval_tmp.end:
                if interval_new.end > interval_tmp.end: # There is overlapping and need to extend the right bound
                    interval_tmp.end = interval_new.end
            else: # No more overlapping with interval_tmp, can add it to the final result
                result.append(interval_tmp)
                interval_tmp = interval_new
                if i > start + 1:
                    break
        result.append(interval_tmp)
        result += intervals[i+1:]
        return result
        
        
if __name__ == "__main__":
    intervals = [Interval(p[0], p[1]) for p in [[1,2],[3,5],[6,7],[8,10],[12,16]]]
    newInterval = Interval(4,9)
    #intervals = [Interval(p[0], p[1]) for p in [[1, 5]]]
    #newInterval = Interval(6,8)
    intervals = [Interval(p[0], p[1]) for p in [[0,5],[9,12]]]
    newInterval = Interval(7,16)
    print(Solution()._bisect(intervals, newInterval))
    
    x = Solution().insert(intervals, newInterval)
    for interval in x:
        print("[{0}, {1}], ".format(interval.start, interval.end))
                
        
