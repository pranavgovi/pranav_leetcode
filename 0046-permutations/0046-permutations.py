class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        []
[1]    [2]    [3]
[1,2] [1,3]  [2,3] [2,1]  [3,1] [3,2]
1,2,3   1,3,2  2,3,1  2,1,3  3,1,2   3,2,1
for n=1, 1
for n=2, 2
for n=3, 6
for n=4, 12 n

        """
        n=len(nums)
        ans = []
        def permutation(path):
            if len(path)==n:
                ans.append(path.copy())
                return
            
            for i in range(n):
                if nums[i] not in visited:
                    path.append(nums[i])
                    visited.add(nums[i])
                    permutation(path)
                    visited.remove(nums[i])
                    path.pop()
        visited=set()
        permutation([])
        return ans


