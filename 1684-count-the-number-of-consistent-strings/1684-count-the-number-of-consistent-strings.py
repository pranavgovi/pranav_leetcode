class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        lookup=set()
        for i in allowed:
            lookup.add(i)
        ans=0
        for word in words:
            flip=True
            for i in word:
                if i not in lookup:
                    flip=False
            if flip:
                ans+=1
        return ans
            
            