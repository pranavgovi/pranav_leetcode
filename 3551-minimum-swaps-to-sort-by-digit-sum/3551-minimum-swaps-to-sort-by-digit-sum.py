class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        #minimum swaps to sort an arr

        """
        compute the sum of each nums and try to generate the order
        """
        def sum_digit(num):
            ans=0
            while num:
                ans+=num%10
                num=num//10
            return ans

        n=len(nums)
        sorted_order=[]
        for ind,val in enumerate(nums):
            s = sum_digit(val)
            sorted_order.append([s, val])
        sorted_order.sort()
    

        having_pos_to_num ={}
        having_num_to_pos={}
        for i in range(n):
            having_pos_to_num[i] = nums[i]
            having_num_to_pos[nums[i]]=i
        needed_pos_to_num={}
        needed_num_to_pos ={}
        for i in range(n):
            needed_pos_to_num[i] =sorted_order[i][1]

        swaps=0
        for i in range(n):
            #at index i what is value needed
            if having_pos_to_num[i] == needed_pos_to_num[i]:
                continue
            else:
                swaps+=1
                value_needed = needed_pos_to_num[i]
                #this is the value that needs to be present at index i
                actual_value_present = having_pos_to_num[i]
                #some other value is present at index i
                ind = having_num_to_pos[value_needed]
                #the value that is needed is present at ind
                #now swap the actual value present to ind
                #value needed to index i
                having_pos_to_num[ind] = actual_value_present
                having_num_to_pos[actual_value_present]= ind
                having_pos_to_num[i]= value_needed
                having_num_to_pos[value_needed] = i
        return swaps 



            
