#include "bits/stdc++.h"
using namespace std;

class Solution {
public:
    int minElements(vector<int>& nums, int limit, int goal) {
        long long ans = 0;
        for (int i: nums)
            ans += i;
        ans = abs(goal - ans);
        ans = ans / limit + (ans % limit ? 1 : 0);
        return ans;
    }
};

int main()
{
    vector<int> nums{1, -1, 1};
    int limit = 3;
    int goal = -4;
    cout << Solution().minElements(nums, limit, goal) << endl;
}