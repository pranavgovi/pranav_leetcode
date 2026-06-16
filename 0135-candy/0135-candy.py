class Solution:
    def candy(self, nums: List[int]) -> int:
        """
        min candy to be given to a child =1
        left to right, make sure than nums[i] is given crct compared to nums[i-1]
        right to left, nums[i] is given crct compared to nums[i+1]
        if a particiulr children has been crct to both left and right, it should be crct?

        [1, 0,2]
        2, 1, 2

        """
        n =len(nums)
        candies = [1]*n
        for i in range(1, n):
            if nums[i]>nums[i-1]:
                candies[i] = candies[i-1]+1
        #i , i+1
        for i in range(n-2, -1, -1):
            if nums[i]> nums[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
        return sum(candies)
        
