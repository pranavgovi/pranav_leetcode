class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
      
        lookup1=defaultdict(int)
        ans2=[]
        lookup2 = set(arr2)
        for i in arr1:
            if i not in lookup2:
                ans2.append(i)
            else:
                lookup1[i]+=1
        
        print(lookup1)
        n=len(arr1)
        ans= []
        j=0
        for i in arr2:
            
            value = lookup1[i]
            for _ in range(value):
                ans.append(i)
        
       
        ans2.sort()
        return ans + ans2

        
        
        
