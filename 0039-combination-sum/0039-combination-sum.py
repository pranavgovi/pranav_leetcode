class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n=len(candidates)
        answer=[]
        def generate(index, path, curr_sum):
            if curr_sum==target:
                answer.append(path.copy())
                return
            
            if curr_sum>target or index==n:
                return
            
            for i in range(index, n):
                if curr_sum + candidates[i]>target:
                    break
                path.append(candidates[i])
                generate(i, path, curr_sum+candidates[i])
                path.pop()
            return
        generate(0, [], 0)
        return answer



                                                                                             