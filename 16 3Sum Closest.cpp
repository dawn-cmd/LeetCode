#include <bits/stdc++.h>
using namespace std;
class Solution {
private:
    int findCloset(const int &target, const vector<int> &nums, int &st, int &ed) {
        int ans = 0x3f3f3f3f;
        int tmp;
        while (st < ed) {
            tmp = nums[st] + nums[ed];
            ans = abs(target - ans) < abs(target - tmp) ? ans : tmp;
            if (tmp > target)
                ed--;
            else if (tmp < target)
                st++;
            else
                break;
        }
        return ans;
    }

public:
    int threeSumClosest(vector<int> &nums, int target) {
        sort(nums.begin(), nums.end());
        int ans = 0x3f3f3f3f;
        for (int i = 0, st, ed, tmp; i < nums.size() - 2; ++i) {
            st = i + 1;
            ed = nums.size() - 1;
            tmp = findCloset(target - nums[i], nums, st, ed) + nums[i];
            ans = abs(ans - target) < abs(tmp - target) ? ans : tmp;
            if (ans == target) return ans;
        }
        return ans;
    }
};

int main() {
}
