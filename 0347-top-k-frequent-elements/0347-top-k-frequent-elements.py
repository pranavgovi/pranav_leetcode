class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        #I am thinking of using a freq bucket
        lookup=defaultdict(int)
        for num in nums:
            lookup[num]+=1
        n=len(nums)
        freq_bucket = [[] for _ in range(n+1)]
        for key,value in lookup.items():
            freq_bucket[value].append(key)
            
        answer=[]
        count=0
        for i in range(n,-1,-1):
            
            if freq_bucket[i]:
                for val in freq_bucket[i]:
                    if count==k:
                        return answer
                    answer.append(val)
                    count+=1
        return answer


        

