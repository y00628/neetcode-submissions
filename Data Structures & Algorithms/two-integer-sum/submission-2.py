class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {} # store num, idx
        vals = set(nums)

        for i, num in enumerate(nums):
            comp[num] = i

        for i, num in enumerate(nums):
            val = target - num
            if val in vals and i != comp[val]:
                return [i, comp[val]]



        