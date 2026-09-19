class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        #x1<=x<=x2
        #y1<=y<=y2
        #eqn of circle (x-h)sq + (y-k)sq = r**2

        # for x in range(x1, x2+1):
        #     for y in range(y1, y2+1):
        #         a = (x-xCenter)**2
        #         b = (y-yCenter)**2
        #         if a+b <=(radius)**2:
        #             return True
        # return False

        #first lets say we identify the closest point on rectange making a contact with the circle
        x_closest= 0 
        y_closest=0
        if xCenter<x1:
            #this means the closest x coordinate is x1
            x_closest =x1
        elif x1<=xCenter<=x2:
            x_closest = xCenter
        else:
            x_closest = x2
        if yCenter<y1:

            y_closest =y1
        elif y1<=yCenter<=y2:
            y_closest = yCenter
        else:
            y_closest = y2
        
        #if we find the point that overlaps with rectangle
        #that overlap point's distance from center should be less than or equal to radius
        a= (xCenter-x_closest)**2
        b = (yCenter- y_closest)**2
        if a+b> (radius**2):
            return False
        return True
