#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {

        vector<vector<int>> adj(numCourses);
        vector<int> indegree(numCourses, 0);
        queue<int> remaining;
        vector<int> result;

        // build adj list + indegree
        for (auto& prereq: prerequisites) {
            adj[prereq[1]].push_back(prereq[0]);
            indegree[prereq[0]]++;
        }

        // add those without prereq to queue
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                remaining.push(i);
            }
        }

        // going through the topological sort
        while (!remaining.empty()) {
            int course = remaining.front();
            remaining.pop();
            result.push_back(course);

            for (auto& neighbor: adj[course]) {
                indegree[neighbor]--;

                if (indegree[neighbor] == 0) {
                    remaining.push(neighbor);
                }
            }
        }

        if (result.size() == numCourses) {
            return result;
        }

        return {};

    }
};
