class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        lookup1=[0]*26
        for i in s:
            ind = ord(i)-ord('a')
            lookup1[ind]+=1
        lookup2=[0]*26
        for i in t:
            ind = ord(i)-ord('a')
            lookup2[ind]+=1
        if lookup1==lookup2:
            return True
        return False