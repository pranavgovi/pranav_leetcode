class Solution:
    def countBits(self, n: int) -> List[int]:
        answer=[0]*(n+1)
        """
        0 :0
        1:1
        2:10
        3:11
        4:100
        101
        """
        memo={0:0, 1:1, 2:1}
        for i in range(n+1):
            if i in memo:
                answer[i] = memo[i]
            else:
                if i%2==0:
                    answer[i] = answer[i//2]
                else:
                    answer[i]= answer[i//2]+1
        return answer

