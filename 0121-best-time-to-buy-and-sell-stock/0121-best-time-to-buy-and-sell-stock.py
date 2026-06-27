class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        len =0,1 return 0
        """
        if len(prices)==0 or len(prices)==1:
            return 0
        
        buy =float('inf')
        max_profit = 0
        for price in prices:
            if price<buy:
                buy = price
            else:
                max_profit = max(max_profit, price-buy)
        return max_profit
            