class DetectSquares:

    def __init__(self):
        self.points=defaultdict(int)


    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1
    
    def count(self, point: List[int]) -> int:
        answer=0
        #for a point check if there is a diagonal point except self
        x1 , y1= point
        for p, count in self.points.items():
            x2, y2 = p
            if abs(x1-x2) == abs(y1-y2) and x1!=x2:
                #this is a diagonal point
                if (x2, y1) in self.points and (x1, y2) in self.points:
                   answer+=(
                    count*self.points[(x2, y1)]*self.points[(x1,y2)]
                   ) 

        return answer


        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)