class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        n=len(nums)
        right=n-1

        answer = [0]*n
        i=0
        while left<=right: #only one value is prcessed so left can be equal to right
            if abs(nums[left])>=abs(nums[right]):
                answer[i] = nums[left]**2
                left+=1
            else:
                answer[i] =  nums[right]**2
                right-=1
    
            i+=1
        answer.reverse()
        return answer
