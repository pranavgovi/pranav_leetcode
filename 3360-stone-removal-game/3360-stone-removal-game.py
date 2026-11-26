class Solution:
    def canAliceWin(self, n: int) -> bool:
        
        removal = 10

        alice =True

        while n>=removal:
            
            if alice:
                alice= False

            else:
                alice = True
            n-=removal
            removal-=1
        if alice:
            return False
        else:
            return True
        