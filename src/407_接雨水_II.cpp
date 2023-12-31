#include <bits/stdc++.h>
#define LL long long
using namespace std;
class Solution {
public:
    int trapRainWater(vector<vector<int>> &heightMap) {
        int n = heightMap.size();
        int m = heightMap[0].size();
        vector<vector<int>> waters(n, vector<int>(m, 0x3f3f3f3f));
        priority_queue<pair<int, int>> q;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (i == 0 || i == n - 1 || j == 0 || j == m - 1) {
                    waters[i][j] = heightMap[i][j];
                    q.emplace(-waters[i][j], i * m + j);
                }
        vector<int> dir{-1, 0, 1, 0, -1};
        while (!q.empty()) {
            int x = q.top().second / m;
            int y = q.top().second % m;
            q.pop();
            for (int i = 0; i < 4; ++i) {
                int nx = x + dir[i];
                int ny = y + dir[i + 1];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if (waters[nx][ny] == heightMap[nx][ny]) continue;
                if (waters[nx][ny] <= waters[x][y]) continue;
                waters[nx][ny] = max(heightMap[nx][ny], waters[x][y]);
                q.emplace(-waters[nx][ny], nx * m + ny);
            }
        }
        int res = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                res += waters[i][j] - heightMap[i][j];
        return res;
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    vector<vector<int>> tmp{{12, 13, 1, 12}, {13, 4, 13, 12}, {13, 8, 10, 12}, {12, 13, 12, 12}, {13, 13, 13, 13}};
    cout << Solution().trapRainWater(tmp) << '\n';
}
