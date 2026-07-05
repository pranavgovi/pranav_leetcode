class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)

        answer=[]
        def generate(index, path):

            if index==n:
                answer.append(path.copy())
                return
            
            #for every index , we can include or exclude
            path.append(nums[index])
            generate(index+1, path)
            path.pop()
            generate(index+1, path)
            return
        generate(0,[])
        return answer