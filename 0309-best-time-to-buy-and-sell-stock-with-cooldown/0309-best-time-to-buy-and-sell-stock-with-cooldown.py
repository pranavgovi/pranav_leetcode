class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #this problem is can be broken down into subproblem of deciding to buy/sell/skip on a particlaur day

        memo={}
        # n=len(prices)
        # def dp(ind, need_to_buy):
        #     if (ind, need_to_buy) in memo:
        #         return memo[(ind, need_to_buy)]
        #     if ind>=n:
        #         memo[(ind, need_to_buy)] =0
                
        #         return 0
            
        #     #for a particlaur ind we can just kip
        #     choice1= dp(ind+1, need_to_buy)
        #     choice2=0
        #     if need_to_buy:
        #         #this means have to buy cant sell
        #         choice2 = -prices[ind] + dp(ind+1, False)
            
        #     else:
        #         #we have to sell
        #         choice2 = prices[ind] + dp(ind+2, True)
        #     memo[(ind, need_to_buy)] = max(choice1, choice2)
        #     return max(choice1, choice2)
        # return dp(0, True)
        n=len(prices)
        dp = [ [0]*(2) for _ in range(n+2)]
        for i in range(n-1,-1,-1):
            for j in range(2):
                op1= dp[i+1][j]
                op2=0
                if j==0:
                    #this is basically we have to buy
                    op2 = -prices[i] + dp[i+1][1]
                else:
                    op2 = prices[i] + dp[i+2][0]
                dp[i][j] = max(op1, op2)
        return dp[0][0]
                    #we can sell
                 
