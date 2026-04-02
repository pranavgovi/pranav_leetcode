class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        1 2 3 0 0 0
              m
        2 5 6 
        """

        n1=len(nums1)
        n2=len(nums2)
        left, right=m-1, n-1
        ptr= m+n-1

        while ptr>=0:
            if left>=0 and right>=0 and nums1[left]>=nums2[right]:
                nums1[ptr]=nums1[left]
                left-=1
            
            else:
                if right>=0:
                    nums1[ptr] = nums2[right]
                    right-=1
            ptr-=1
        


        