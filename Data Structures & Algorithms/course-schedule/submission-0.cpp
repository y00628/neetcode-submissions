#include <iostream>
#include <unordered_map>
#include <queue>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // a: 15618
        // b: 15213

        // b -> a: b is the key, a is in the value list

        // adj: {node: next ones} => unordered_map<>
        unordered_map<int, vector<int>> adj;
        unordered_map<int, int> indegree;
        queue<int> q;
        int count = 0;

        // build adj + indegree from prerequisites
        for (auto& prereq: prerequisites) {
            adj[prereq[1]].push_back(prereq[0]);
            indegree[prereq[0]]++;
        }

        // seed queue: all nodes where indegree == 0
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) q.push(i);
        }

        while (!q.empty()) {
            int node = q.front();
            q.pop();
            count++;

            for (auto& neighbor: adj[node]) {
                indegree[neighbor] -= 1;
                if (indegree[neighbor] == 0) q.push(neighbor);
            }
        }


        
        
        // while queue not empty:
        //     pop node, append to result
        //     for each neighbor in adj[node]:
        //         indegree[neighbor] -= 1
        //         if indegree[neighbor] == 0: push to queue

        return count == numCourses;
    }
};
