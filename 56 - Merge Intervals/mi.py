# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        n = len(intervals)
        if n == 0:
            return []
        intervals_sorted = sorted(intervals, key = lambda interval: interval.start) # Sort the intervals according to the left end
        
        result = []
        interval_tmp = intervals_sorted[0]
        for i in range(1, n):
            interval_new = intervals_sorted[i]
            if interval_new.start <= interval_tmp.end:
                if interval_new.end > interval_tmp.end: # There is overlapping and need to extend the right bound
                    interval_tmp.end = interval_new.end
            else: # No more overlapping with interval_tmp, can add it to the final result
                result.append(interval_tmp)
                interval_tmp = interval_new
        result.append(interval_tmp)
        
        return result
        
if __name__ == "__main__":
    intervals = [Interval(p[0], p[1]) for p in [[1,4],[2,3]]]
    x = Solution().merge(intervals)
    for interval in x:
        print("[{0}, {1}], ".format(interval.start, interval.end))
