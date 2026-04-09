class Solution:
    def countAndSay(self, n: int) -> str:
        
        def group(given_str):

            answer=''
            i=0
            n=len(given_str)
            while i<n:
                count=1
                while i+1<n and given_str[i]==given_str[i+1]:
                    count+=1
                    i+=1

                answer+=str(count)
                answer+=given_str[i]
                i+=1
            return answer
        ans = '1'
        for i in range(2,n+1):
            ans = group(ans)
        return ans