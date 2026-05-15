class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}  # num -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in comp:
                return [comp[complement], i]
            comp[num] = i