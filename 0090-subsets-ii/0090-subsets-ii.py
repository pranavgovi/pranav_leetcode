class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans = []

        def generate(index):

            if index==n:
                ans.append(path.copy())
                return
            

            path.append(nums[index]) #I am including it
            generate(index+1)
            path.pop()
            #I am skipping it here
            index+=1
            while index<n and nums[index]==nums[index-1]:
                index+=1
            generate(index)
            
        path=[]
        generate(0)
        return ans