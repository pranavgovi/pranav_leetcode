class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup=defaultdict(list)
        for s in strs:
            signature =[0]*26
            for i in s:
                signature[ord(i)-ord('a')]+=1
            lookup[tuple(signature)].append(s)
        return list(lookup.values())