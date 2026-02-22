class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        #97-122

        ans=''
        for word in words:
    
            total=0
            for i in word:
                total+= weights[ord(i)-97]
            
            total= total%26
            ans+= chr(122-total)
        return ans





