class DetectSquares:

    def __init__(self):
        self.lookup = {}

    def add(self, point: List[int]) -> None:
        pt=tuple(point)
        if pt not in self.lookup:
            self.lookup[pt]=0
        self.lookup[tuple(point)]+=1


    def count(self, point: List[int]) -> int:
        #go over checking every single diagonal pt
        #cumukate the ways
        ways=0
        x1, y1= point
        for pt, count in self.lookup.items():
            x2, y2 = pt
            if abs(x1-x2)==abs(y1-y2) and x1!=x2:
                #x2,y2 is a diagonal pt to x1,y1
                if (x1,y2) in self.lookup and (x2,y1) in self.lookup:
                    ways+= (self.lookup[(x2, y2)] * self.lookup[(x2,y1)]* self.lookup[(x1,y2)])
        return ways


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)