#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<string>> ans;
    void dfs(vector<int> &g, int row) {
        if (row == g.size()) {
            vector<string> tmp(g.size());
            for (int i = 0; i < g.size(); ++i) {
                string s = "";
                for (int j = 0; j < g.size(); ++j) s += (j == g[i] ? 'Q' : '.');
                tmp[i] = s;
            }
            ans.emplace_back(tmp);
            return;
        }
        for (int i = 0; i < g.size(); ++i) {
            int legal = 1;
            for (int j = 0; j < row; ++j) {
                if (i == g[j] || abs(i - g[j]) == abs(row - j)) {
                    legal = 0;
                    break;
                }
            }
            if (!legal) continue;
            g[row] = i;
            dfs(g, row + 1);
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        vector<int> g(n, 0x3f3f3f3f);
        dfs(g, 0);
        return ans;
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<vector<string>> tmp = Solution().solveNQueens(9);
    for (const auto &item: tmp) {
        for (const auto &s: item) cout << s << '\n';
        cout << '\n';
    }
}

