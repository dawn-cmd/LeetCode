#include <bits/stdc++.h>
using namespace std;
#define LL long long
class Solution {
public:
    vector<vector<int>> fourSum(vector<int> &nums, int target) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        if (nums.size() < 4) return ans;
        for (int i = 0; i < nums.size(); ++i) {
            if (i && nums[i] == nums[i - 1]) continue;
            for (int j = i + 1; j < nums.size(); ++j) {
                if (j - i - 1 && nums[j] == nums[j - 1]) continue;
                int l = j + 1;
                int r = nums.size() - 1;
                while (l < r) {
                    if ((LL) nums[i] + (LL) nums[j] < (LL) target - (LL) nums[l] - (LL) nums[r]) {
                        ++l;
                        continue;
                    }
                    if ((LL) nums[i] + (LL) nums[j] > (LL) target - (LL) nums[l] - (LL) nums[r]) {
                        --r;
                        continue;
                    }
                    ans.emplace_back(vector<int>{nums[i], nums[j], nums[l], nums[r]});
                    while (l < r && nums[l] == nums[l + 1]) ++l;
                    while (l < r && nums[r] == nums[r - 1]) --r;
                    ++l;
                    --r;
                }
            }
        }
        return ans;
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<int> tmp{1000000000, 1000000000, 1000000000, 1000000000};
}
