class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        crosses = set()
        crosses.update(self.getCrossPoints(A, B, C, D, E, F, E, H))
        crosses.update(self.getCrossPoints(A, B, C, D, E, H, G, H))
        crosses.update(self.getCrossPoints(A, B, C, D, G, H, G, F))
        crosses.update(self.getCrossPoints(A, B, C, D, G, F, E, F))
        crosses.update(self.getCrossPoints(E, F, G, H, A, B, A, D))
        crosses.update(self.getCrossPoints(E, F, G, H, A, D, C, D))
        crosses.update(self.getCrossPoints(E, F, G, H, C, D, C, B))
        crosses.update(self.getCrossPoints(E, F, G, H, C, B, A, B))
        
        area_sum =(C - A) * (D - B) + (G - E) * (H - F)
        if len(crosses) < 4:
            return area_sum
        else:
            X = list({point[0] for point in crosses})
            Y = list({point[1] for point in crosses})
            return area_sum - abs(X[1] - X[0]) * abs(Y[1] - Y[0])
        
    # Get the cross points of a horizontal or vertical line segment defined by X1, Y1, X2, Y2 and a rectangle defined by A, B, C, D
    def getCrossPoints(self, A, B, C, D, X1, Y1, X2, Y2):
        if Y1 == Y2:
            if X1 > X2:
                X1, X2 = X2, X1
        if X1 == X2:
            if Y1 > Y2:
                Y1, Y2 = Y2, Y1
        cross = set()
        if (X2 < A) or (X1 > C) or (Y2 < B) or (Y1 > D):
            return set()
        elif Y1 == Y2: # A horizontal line
            if X2 <= C:
                cross.add((X2, Y1))
            else:
                cross.add((C, Y1))
                
            if X1 >= A:
                cross.add((X1, Y1))
            else:
                cross.add((A, Y1))
        elif X1 == X2: # A vertical line
            if Y2 <= D:
                cross.add((X1, Y2))
            else:
                cross.add((X1, D))
                
            if Y1 >= B:
                cross.add((X1, Y1))
            else:
                cross.add((X1, B))
        return cross
if __name__ == "__main__":
    A, B, C, D, E, F, G, H = -3, 0, 3, 4, 0, -1, 9, 2
    #A, B, C, D, E, F, G, H = -5, -2, 3, 1, -3, -3, 3, 3
    print(Solution().computeArea(A, B, C, D, E, F, G, H))
