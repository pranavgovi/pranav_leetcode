class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        """
        usually we think which ballon to burst first
        if we proceed in tht direction neighbors frequently change
        so in a given range why not consider burst a ballon in the end
        """
        #to avoid errors append both the sides
        nums=[1]+nums+[1]
        n=len(nums)
        memo={}

        def dfs(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            maxi =0
            for i in range(left, right+1):
                #burst the current ballon last
                curr_coins = nums[i]*nums[left-1]*nums[right+1]
                tot_coins = curr_coins + dfs(left,i-1) + dfs(i+1,right)
                maxi= max(maxi, tot_coins)
            memo[(left, right)]= maxi
            return maxi
        return dfs(1, n-2)




