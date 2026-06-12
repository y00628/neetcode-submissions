class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false; // edge case check

        array<int, 26> s1_cnt{}, s2_cnt{}; // init
        int n = s1.size(); // length of s1

        // init distribution
        for (int i = 0; i < n; i++) {
            s1_cnt[s1[i] - 'a']++;
            s2_cnt[s2[i] - 'a']++;
        }

        if (s1_cnt == s2_cnt) return true; // init check

        // subsequent check
        for (int i = 1; i <= (int)s2.size() - n; i++) {
            s2_cnt[s2[i-1] - 'a']--;
            s2_cnt[s2[i+n-1] - 'a']++;
            if (s1_cnt == s2_cnt) return true;
        }

        return false;
    }
};