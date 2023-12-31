#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int findMaxValueOfEquation(vector<vector<int>> &points, int k) {
        using pii = pair<int, int>;
        priority_queue<pii, vector<pii>> heap;
        int ans = -0x3f3f3f3f;
        for (const auto &cur: points) {
            int x = cur[0], y = cur[1];
            while (!heap.empty() && x - heap.top().second > k) heap.pop();
            if (!heap.empty()) ans = max(ans, x + y + heap.top().first);
            heap.emplace(y - x, x);
        }
        return ans;
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<vector<int>> tmp{{1, 3}, {2, 0}, {5, 10}, {6, -10}};
    int k = 1;
    cout << Solution().findMaxValueOfEquation(tmp, k) << '\n';
}
