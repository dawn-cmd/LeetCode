#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minimumIncompatibility(vector<int>& nums, int k) {
        unordered_map<int, int> val;
        int n = nums.size();
        int group_size = n / k;
        for (int cur = 1; cur < (1 << n); ++cur) {
            if (bitset<32>(cur).count() != group_size) continue;
            int minn = 0x3f3f3f3f;
            int maxn = -0x3f3f3f3f;
            unordered_set<int> vis;
            for (int i = 0; i < n; ++i) {
                if (!((1 << i) & cur)) continue;
                if (vis.count(nums[i])) break;
                vis.insert(nums[i]);
                minn = min(minn, nums[i]);
                maxn = max(maxn, nums[i]);
            }
            if (vis.size() != group_size) continue;
            val[cur] = maxn - minn;
        }
        vector<int> dp(1 << (n + 1), 0x3f3f3f3f);
        dp[0] = 0;
        for (int cur = 0; cur < (1 << n); ++cur) {
            if (dp[cur] == 0x3f3f3f3f) continue;
            unordered_map<int, int> space;
            for (int i = 0; i < n; ++i) {
                if ((1 << i) & cur) continue;
                space[nums[i]] = i;
            }
            if (space.size() < group_size) continue;
            int sub = 0;
            for (const auto &item: space) sub |= 1 << item.second;
            for (int tmp = sub; tmp; tmp = (tmp - 1) & sub) {
                if (val.find(tmp) == val.end()) continue;
                dp[cur | tmp] = min(dp[cur | tmp], dp[cur] + val[tmp]);
            }
        }
        return dp[(1 << n) - 1] == 0x3f3f3f3f ? -1 : dp[(1 << n) - 1];
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<int> tmp{6,8,5,16,8,12,11,7,13,16,15,14,7,9,1,10};
    cout << Solution().minimumIncompatibility(tmp, 4);
}
