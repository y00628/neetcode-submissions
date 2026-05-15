class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums) # [-1,0,1,2,-1,-4] -> [-4, -1, -1, 0, 1, 2]
        res = []

        for i in range(len(nums)):
            target = -nums[i]

            l, r = i+1, len(nums)-1

            while l < r:
                if nums[l] + nums[r] == target and (nums[i], nums[l], nums[r]) not in res:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return res

            