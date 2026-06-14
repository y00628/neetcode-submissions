#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        // zip and sort by position descending (closest to target first)
        vector<pair<int,int>> cars;
        for (int i = 0; i < position.size(); i++)
            cars.push_back({position[i], speed[i]});

        sort(cars.begin(), cars.end(), [](const auto& a, const auto& b) {
            return a.first > b.first;
        });

        // time for each car to reach target
        stack<double> st;
        for (auto& [pos, spd] : cars) {
            double time = (double)(target - pos) / spd;
            // if this car takes longer than the one ahead, it's a new fleet
            if (st.empty() || time > st.top())
                st.push(time);
        }

        return st.size();
    }
};

