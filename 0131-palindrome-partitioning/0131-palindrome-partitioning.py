class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def check_pal(left, right):
            #this function checks if arr[left:right+1] is a palindrome or not

            while left<=right:
                if s[left]!=s[right]:
                    return False
                else:
                    left+=1
                    right-=1
            return True

        ans =[]
        n = len(s)
        path = []
        def generate(ind, path):
            if ind==n:
                ans.append(path.copy())
                return
            if ind>n:
                return 
            
            for i in range(ind,n):
                if check_pal(ind,i):
                    path.append(s[ind:i+1])
                    generate(i+1, path)
                    path.pop()
        generate(0,[])
        return ans



            


