class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #for any triplet if a number is greater than target they wont form the target we can skip them
        seen=set()
        cnt=0
        for triplet in triplets:
            a,b,c = triplet
            if a>target[0] or b>target[1] or c>target[2]:
                continue
            if a==target[0] and 0 not in seen:
                seen.add(0)
                cnt+=1
            if b==target[1] and 1 not in seen:
                seen.add(1)
                cnt+=1
            if c==target[2] and 2 not in seen:
                seen.add(2)
                cnt+=1
        if cnt==3:
            return True 
        return False
