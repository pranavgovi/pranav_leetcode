class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        #first check how many common items , extra items
        common =  min(need1, need2)
        extra = max(need1, need2)-common
        if need1>=need2:
            extra_cost = cost1
        else:
            extra_cost = cost2
        #for this common , we can either use costboth or buy them separetly
        common_price = common*(min(costBoth,(cost1+cost2)))
        extra_price = extra*(min(extra_cost, costBoth))
        return common_price+extra_price
        
      