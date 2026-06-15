class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        left, right = 0, 1
        curr_sum = nums[0]

        while right < len(nums):
            if curr_sum < target:
                curr_sum += nums[right]
                right += 1
            else:
                min_length = min(min_length, right - left)  # right already 1 ahead
                curr_sum -= nums[left]
                left += 1
        

        # drain remaining valid windows
        while curr_sum >= target:
            min_length = min(min_length, right - left)
            curr_sum -= nums[left]
            left += 1


        if min_length == float('inf'):
            return 0

        return min_length