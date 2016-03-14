
"""

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.

"""

### beat 88%
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
        area1 = (C-A)*(D-B)
        area2 = (H-F)*(G-E)
        side1 = self.computeSide(A, C, E, G)
        side2 = self.computeSide(B, D, F, H)
        return area1+area2-side1*side2
    
    def computeSide(self,a,b,c,d):
        if d < a or c > b:
            return 0
        elif c > a and d <= b:
            return d-c
        elif c <= a and d <= b:
            return d-a
        elif c <= a and d > b:
            return b-a    
        else:
            return b-c
    

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
        area1 = (C-A)*(D-B)
        area2 = (H-F)*(G-E)
        commonarea = max(0, min(C,G)-max(A,E))*max(0, min(D,H)-max(B,F))
        return area1+area2-commonarea
    

