class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Use cmp_to_key when the order depends on comparing TWO elements together (pairwise comparison), not just one element’s properties.
        """
        def compare(a,b):
            if a+b> b+a:
                #a should come first
                return -1
            else:
                return 1
            
        nums = list(map(str, nums)) #map the function to the iterable array
        nums.sort(key = cmp_to_key(compare)) #do a custom sort
        if nums[0]=='0':
            return '0'
        return ''.join(nums)
