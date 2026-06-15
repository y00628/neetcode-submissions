class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int min_length = INT_MAX;
        int left = 0;
        int right = 1;
        int curr_sum = nums[0];

        while (right < nums.size()) {
            if (curr_sum < target) {
                curr_sum += nums[right++];
            } else {
                min_length = min(min_length, right-left);
                curr_sum -= nums[left++];
            }
        }

        while (curr_sum >= target) {
            min_length = min(min_length, right-left);
            curr_sum -= nums[left++];
        }

        return min_length == INT_MAX ? 0 : min_length;
    }
};