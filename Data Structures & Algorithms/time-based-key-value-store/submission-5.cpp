class TimeMap {
public:
    unordered_map<string, vector<pair<string, int>>> timeMap;
    
    void set(string key, string value, int timestamp) {
        timeMap[key].push_back({value, timestamp});
    }
    
    string get(string key, int timestamp) {
        int lo = 0;
        int hi = timeMap[key].size() - 1;
        int res = -1;

        if (timeMap[key].empty()) {
            return "";
        }

        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (timeMap[key][mid].second <= timestamp) {
                res = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        if (res == -1) {
            return "";
        }

        return timeMap[key][res].first;
    }
};
