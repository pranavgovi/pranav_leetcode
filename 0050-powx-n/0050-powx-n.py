class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        neg=False
        if n<0:
            neg=True
            n=-1*n
        base =x
        power = n
        tot=1
        while power>1:
            if power%2!=0:
                power-=1
                tot*=base
            power= power//2
            base = base*base
        if neg:
            return 1/(tot*base)        
        return tot*base



