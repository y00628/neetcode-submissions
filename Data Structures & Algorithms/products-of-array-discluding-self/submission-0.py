class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix: 2x4x6
        
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        res = [0] * n

        for i in range(1, len(nums)):
            prefix[i] = nums[i-1]*prefix[i-1]

        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1]*suffix[i+1]

        # print(prefix)
        # print(suffix)

        for i in range(n):
            res[i] =  prefix[i]*suffix[i]

        return res