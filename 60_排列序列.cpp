#include <bits/stdc++.h>
using namespace std;
class Solution {
private:
    int cnt;
    string ans;
    void dfs(vector<int> &h, int step, int k, string cur) {
        if (step == h.size() - 1) {
            ++cnt;
            if (cnt == k) ans = cur;
            return;
        }
        if (cnt >= k) return;
        for (int i = 1; i < h.size(); ++i) {
            if (h[i]) continue;
            h[i] = 1;
            dfs(h, step + 1, k, cur + (char)('0' + i));
            h[i] = 0;
        }
    }

public:
    string getPermutation(int n, int k) {
        vector<int> h(n + 1, 0);
        dfs(h, 0, k, "");
        return ans;
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout << Solution().getPermutation(4, 9) << '\n';
}

