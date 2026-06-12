class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();

        // cout << m << "," << n << endl;

        int low = 0;
        int high = m*n-1;
        int mid = (low + high) / 2;

        while (low <= high) {
            mid = (low + high) / 2;
            int curr = matrix[mid/n][mid%n];
            if (curr == target) {
                return true;
            } else if (curr > target) {
                high = mid-1;
            } else {
                low = mid+1;
            }
        }

        return false;
    }
};
