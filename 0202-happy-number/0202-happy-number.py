class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            st = str(n)
            tot =0
            for i in st:
                tot+= (int(i)**2)
            
            n=tot
        if n==1:
            return True
        return False
