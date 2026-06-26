class Solution {
private:
    unsigned long long math_comb(int n, int k) {
        if (k < 0 || k > n) return 0;
        if (k == 0 || k == n) return 1;
        
        // Optimize by using symmetry: comb(n, k) == comb(n, n-k)
        if (k > n - k) k = n - k; 
        
        long long res = 1;
        for (int i = 1; i <= k; ++i) {
            res = res * (n - i + 1) / i;
        }
        return res;
    }

public:
    int uniquePaths(int m, int n) {
        // use combinatorics
        // int longer = max(m, n);
        // int shorter = min(m, n);
        return math_comb(m+n-2, m-1);
    }
};
