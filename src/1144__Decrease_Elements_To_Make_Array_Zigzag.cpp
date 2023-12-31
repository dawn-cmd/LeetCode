#include "bits/stdc++.h"
#define rep(i, a, b) for (auto i = (a); i < (b); ++i)
#define sz(a) (a).size()
using namespace std;
class Solution {
public:
    int movesToMakeZigzag(const vector<int> &nums) {
        if (sz(nums) == 1) {
            return 0;
        }
        int cnt1 = 0, cnt2 = 0;
        for (int i = 1, tmp; i < sz(nums); i += 2) {
            tmp = nums[i - 1];
            if (i < sz(nums) - 1) {
                tmp = min(tmp, nums[i + 1]);
            }
            cnt1 += max(0, nums[i] - (tmp - 1));
        }
        for (int i = 0, tmp; i < sz(nums); i += 2) {
            if (i == 0) {
                tmp = nums[i + 1];
            } else if (i >= sz(nums) - 1) {
                tmp = nums[i - 1];
            } else {
                tmp = min(nums[i + 1], nums[i - 1]);
            }
            cnt2 += max(0, nums[i] - (tmp - 1));
        }
        return min(cnt1, cnt2);
    }
};
int main() {
    cin.tie(0)->sync_with_stdio(0);
    cout << Solution().movesToMakeZigzag(vector<int>{9, 6, 1, 6, 2}) << '\n';
    return 0;
}
