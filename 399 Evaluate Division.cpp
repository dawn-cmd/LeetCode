#include "bits/stdc++.h"
using namespace std;

class Solution {
public:
    map<string, map<string, double>> his;

    static void addEdge(const string &a, const string &b, double c, map<string, map<string, double>> &g) {
        g[a][b] = c;
        g[b][a] = 1 / c;
    }


    double bfs(const string &st, const string &ed, map<string, map<string, double>> &g) {
        if (!g.count(st) || !g.count(ed))
            return -1;
        if (st == ed)
            return 1;
        queue<pair<string, double>> q;
        map<string, int> h;
        q.emplace(st, 1);
        h[st] = 1;
        while (!q.empty()) {
            pair<string, double> tmp = q.front();
            q.pop();
            string cur = tmp.first;
            double val = tmp.second;
            for (const auto &to: g[cur]) {
                if (h.count(to.first))
                    continue;
                q.emplace(to.first, val * to.second);
                his[st][to.first] = val * to.second;
                h[to.first] = 1;
                if (to.first == ed)
                    return val * to.second;
                if (his.count(to.first) && his[to.first].count(ed))
                    return val * to.second * his[to.first][ed];
            }
        }
        return -1;
    }

    vector<double> calcEquation(vector<vector<string>> &equations, vector<double> &values, vector<vector<string>> &queries) {
        map<string, map<string, double>> g;
        for (int i = 0; i < equations.size(); ++i)
            addEdge(equations[i][0], equations[i][1], values[i], g);
        vector<double> ans(queries.size());
        for (int i = 0; i < queries.size(); ++i)
            ans[i] = bfs(queries[i][0], queries[i][1], g);
        return ans;
    }
};

int main() {
}
