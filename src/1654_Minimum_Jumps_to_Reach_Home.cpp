#include <bits/stdc++.h>
using namespace std;
class item {
public:
    int pos;
    int step;
    bool is_back;
    item(int pos, int step, int is_back) {
        this->pos = pos;
        this->step = step;
        this->is_back = is_back;
    }
};
class Solution {
public:
    int minimumJumps(vector<int> &forbidden, int a, int b, int x) {
        if (x == 0) return 0;
        int max_f = -1;
        for (auto i: forbidden)
            max_f = max(max_f, i);
        int up_bond = max(max_f + a + b, x);
        map<int, int> is_forbid;
        for (auto i: forbidden)
            is_forbid[i] = 1;
        map<int, int> vis;
        vis[0] = 1;
        queue<item> q;
        q.emplace(item(0, 0, 0));
        while (!q.empty()) {
            int pos = q.front().pos;
            int step = q.front().step;
            bool is_back = q.front().is_back;
            //cout << pos << ' ' << step << '\n';
            q.pop();
            int n_pos = pos - b;
            if (!is_back && n_pos >= 0 && !is_forbid[n_pos] && !vis[n_pos]) {
                if (n_pos == x) return step + 1;
                vis[n_pos] = 1;
                q.emplace(item(n_pos, step + 1, 1));
            }
            n_pos = pos + a;
            if (n_pos <= up_bond && !is_forbid[n_pos] && !vis[n_pos]) {
                if (n_pos == x) return step + 1;
                vis[n_pos] = 1;
                q.emplace(item(n_pos, step + 1, 0));
            }
        }
        return -1;
    }
};
int main() {
    vector<int> tmp{162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149, 153, 9, 54, 154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164, 136, 72, 98};
    cout << Solution().minimumJumps(tmp, 29, 98, 80) << '\n';
}
