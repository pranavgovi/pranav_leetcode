class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        1, 1, 2 , 5, 6 ,7 , 10  target=8
        [1] [1] [2] [5] [6] [7] [10]
        in this for i=0, 1 this can trvaerse and add duplicates to its path
        but 1 at i=1 should not start its own branch
[1,1][1,2], [1,5] [1,6] , [1,7] [1,10]
[1,1,2] [1,1,5]..........
        """
        n=len(candidates)
        candidates.sort()
        answer=[]
        def backtrack(currSum, path, index):
            if currSum==target:
                answer.append(path.copy())
                return
            if index==n:
                return
            #this loop's start is index
            start=index
            for i in range(index, n):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if currSum + candidates[i]>target:
                    break
                #If i am not the starting value in a branch and if I am a duplicate kindly skip me
                path.append(candidates[i])
                backtrack(currSum + candidates[i],path, i+1)
                path.pop()
            return
        backtrack(0,[],0)
        return answer