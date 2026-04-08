class Robot:

    def __init__(self, width: int, height: int):
        self.rotation={
            'East': 'North', "North":'West', "West":'South', "South":'East'
        }
        self.walk ={  'East': [1,0], "North":[0,1], "West":[-1,0], "South":[0,-1] }
        self.currDir = "East"
        self.currPos = [0,0]
        self.width= width
        self.height= height
    
    def check(self, a,b):
        
        if a>=self.width or b>=self.height or a<0 or b<0:
            return False
        else:
            return True


    def step(self, num: int) -> None:
        perimeter = 2*(self.width+self.height)-4
        num= num%perimeter
        if num==0:
            num=perimeter
        for step in range(num):
            x1, y1 = self.currPos
            #try to move in the same direction
            #walk in the same direction
            x2, y2 = self.walk[self.currDir]
            while not self.check(x1+x2, y1+y2):
                self.currDir = self.rotation[self.currDir]
                x2, y2 = self.walk[self.currDir]
                
            else:
                #no need to update currDir
                #update currPos
                self.currPos = [x1+x2, y1+y2]
        


    def getPos(self) -> List[int]:
        return self.currPos

    def getDir(self) -> str:
        return self.currDir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()