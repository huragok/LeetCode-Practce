# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        n = len(points)
        if n == 0:
            return 0
        global_max = 0
        for i in range(n): # The first point
            map_slope_to_count = dict()
            for j in range(i+1, n): # The second point
                slope = self._getSlopeTuple(points[j], points[i])
                map_slope_to_count[slope] = map_slope_to_count.setdefault(slope, 0) + 1
                
            overlap = map_slope_to_count.pop((0, 0), 0)
            local_max = 0
            for val in map_slope_to_count.values():
                if val > local_max:
                    local_max = val
            local_max += overlap
            if local_max > global_max:
                global_max = local_max
        return global_max + 1
        
    def _getSlopeTuple(self, point_a, point_b):
        x_dif = point_a.x - point_b.x
        y_dif = point_a.y - point_b.y
        
        if y_dif == 0 and x_dif == 0:
            return (0, 0)
        elif x_dif == 0:
            return (1, 0)
        elif y_dif == 0:
            return (0, 1)
        else:
            gcd = self._getGCD(x_dif, y_dif)
            pair = (y_dif / gcd, x_dif / gcd)
            if pair[1] < 0: # Make sure that the second number is always greater than or equal to 0
                pair = -pair[0], -pair[1]
            return pair
        
    def _getGCD(self, a, b):
        if a % b == 0:
            return b
        else:
            return self._getGCD(b, a % b)
            
if __name__ == "__main__":
    points = [Point(0, 0), Point(1, 1), Point(2, 2), Point(0, 4), Point(1, 3), Point(3, 1)]
    print(Solution().maxPoints(points))
