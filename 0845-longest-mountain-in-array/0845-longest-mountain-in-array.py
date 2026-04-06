class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # before ele ar estricly increasing after tht strictly decreasing
        answer = 0 
        peak_start = -1
        peak_end = -1

        i=0
        n=len(arr)
        while i<n:
            
            if i+1<n and arr[i]<arr[i+1]:
                peak_start = i
                #ride the peak
                while i+1<n and arr[i]<arr[i+1]:
                    i+=1
                #now arr[i+1] is lesser
                #i becomes peak
                peak= i
        
                #ride the downfall
                
                while i+1<n and arr[i]>arr[i+1]:
                    peak_end = i+1
                    i+=1
                #you bave to take when both of them are ture
                if peak_start==-1 or peak_end==-1:
                    continue
                else:
                    answer= max(answer, peak_end-peak_start+1)
            else:
                i+=1
        return answer

                