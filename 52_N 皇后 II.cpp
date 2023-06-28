#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int ans;
    void dfs(int row, int col, int lmove, int rmove, int n) {
        if (row == n) {
            ++ans;
            return;
        }
        int blank = (~(col | lmove | rmove)) & ((1 << n) - 1);
        while (blank) {
            int cur = blank & -blank;
            dfs(row + 1, col | cur, (lmove | cur) << 1, (rmove | cur) >> 1, n);
            blank &= (blank - 1);
        }
    }
    int totalNQueens(int n) {
        ans = 0;
        dfs(0, 0, 0, 0, n);
        return ans;
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout << Solution().totalNQueens(13) << '\n';
}

