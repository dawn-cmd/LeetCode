#include "bits/stdc++.h"
using namespace std;

class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        if (source == destination)
            return true;
        vector<vector<int>> g(n);
        for (vector<int> edge: edges)
        {
            g[edge[0]].push_back(edge[1]);
            g[edge[1]].push_back(edge[0]);
        }
        queue<int> q;
        q.push(source);
        map<int, int> h;
        while(!q.empty())
        {
            int now = q.front();
            q.pop();
            for (int to: g[now])
            {
                if (to == destination)
                    return true;
                if (h[to])
                    continue;
                q.push(to);
                h[to] = 1;
            }
        }
        return false;
    }
};

int main()
{

}