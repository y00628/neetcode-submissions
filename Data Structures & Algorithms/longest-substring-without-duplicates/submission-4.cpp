class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> idx;
        int best = 0, left = 0;

        for (int right = 0; right < s.size(); right++) {
            if (idx.count(s[right]) && idx[s[right]] >= left)
                left = idx[s[right]] + 1;  // jump past previous occurrence
            idx[s[right]] = right;
            best = max(best, right - left + 1);
        }
        return best;
    }
};
