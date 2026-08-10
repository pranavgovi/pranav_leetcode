class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #this problem is can be broken down into subproblem of deciding to buy/sell/skip on a particlaur day

        memo={}
        n=len(prices)
        def dp(ind, need_to_buy):
            if (ind, need_to_buy) in memo:
                return memo[(ind, need_to_buy)]
            if ind>=n:
                memo[(ind, need_to_buy)] =0
                
                return 0
            
            #for a particlaur ind we can just kip
            choice1= dp(ind+1, need_to_buy)
            choice2=0
            if need_to_buy:
                #this means have to buy cant sell
                choice2 = -prices[ind] + dp(ind+1, False)
            
            else:
                #we have to sell
                choice2 = prices[ind] + dp(ind+2, True)
            memo[(ind, need_to_buy)] = max(choice1, choice2)
            return max(choice1, choice2)
        return dp(0, True)



                 
