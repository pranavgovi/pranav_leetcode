class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mini_sum  = nums[0]+nums[1] + nums[2]
        closest_sum = abs(mini_sum-target)
         #always a better thing to initialise rather than 
        #assigning it to float('inf')

        n= len(nums)
        for i in range(n-2):
            curr = nums[i]
            left = i+1
            right=n-1
            while left<right:
                total_sum = curr+ nums[left] + nums[right]
                if total_sum== target:
                    #this should be the closest
                    return target
                
                elif total_sum<target:
                    if abs(total_sum-target)< closest_sum:
                        #valid answer
                        closest_sum = abs(total_sum-target)
                        mini_sum = total_sum

                    #move your left towards right
                    left+=1
                
                else:
                    if abs(total_sum-target)< closest_sum:
                        closest_sum = abs(total_sum-target)
                        mini_sum = total_sum
                    right-=1

                
        return mini_sum