#include <bits/stdc++.h>
#define mp(a, b) make_pair(a, b)
using namespace std;
class Solution {
public:
    int ans;
    void bfs(const vector<vector<int>> &grid, vector<vector<int>> &vis, const int &x, const int &y) {
        if (vis[x][y]) {
            return;
        }
        if (grid[x][y] == 1) {
            return;
        }
        queue<pair<int, int>> q;
        q.push(mp(x, y));
        vector<vector<int>> ds{{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        bool touchEdge = false;
        while (!q.empty()) {
            int curx = q.front().first;
            int cury = q.front().second;
            if (curx == 0 || curx == grid.size() - 1 || cury == 0 || cury == grid[0].size() - 1) {
                touchEdge = true;
            }
            q.pop();
            for (int i = 0; i < 4; ++i) {
                int tmpx = curx + ds[i][0];
                int tmpy = cury + ds[i][1];
                if (!(0 <= tmpx && tmpx < grid.size() && 0 <= tmpy && tmpy < grid[0].size())) {
                    continue;
                }
                if (vis[tmpx][tmpy]) {
                    continue;
                }
                if (grid[tmpx][tmpy] == 1) {
                    continue;
                }
                q.push(mp(tmpx, tmpy));
                vis[tmpx][tmpy] = 1;
                if (tmpx == 0 || tmpx == grid.size() - 1 || tmpy == 0 || tmpy == grid[0].size() - 1) {
                    touchEdge = true;
                }
            }
        }
        if (!touchEdge) {
            ans++;
        }
    }
    int closedIsland(vector<vector<int>> &grid) {
        vector<vector<int>> vis;
        ans = 0;
        for (int i = 0; i < grid.size(); ++i) {
            vis.emplace_back(vector<int>(grid[i].size()));
            for (int j = 0; j < vis[i].size(); ++j) {
                vis[i][j] = 0;
            }
        }
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[i].size(); ++j) {
                bfs(grid, vis, i, j);
            }
        }
        return ans;
    }
};
int main() {
}
