class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearest_x = max(x1,min(x2,xCenter))
        nearest_y = max(y1,min(y2,yCenter))
        
        dist_x = nearest_x - xCenter
        dist_y = nearest_y - yCenter
        return dist_x**2 + dist_y**2 <= radius**2