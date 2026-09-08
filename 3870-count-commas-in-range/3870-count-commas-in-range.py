class Solution:
    def countCommas(self, n: int) -> int:
        """
        n can be in range 1-100,000
        """
    
        if n<1000:
            return 0
        else:
            return n-1000+1
        
            