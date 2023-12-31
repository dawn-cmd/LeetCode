//
// Created by LightString on 1/6/2023.
//
#include "bits/stdc++.h"
using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int l = 0;
        int r = 0;
        int curSum = 0;
        int ans = INT_MAX;
        int n = nums.size();
        x = -x;
        for (const auto &i: nums)
            x += i;
        if (x == 0)
            return n;
        if (x < 0)
            return -1;
        while (r < n)
        {
            curSum += nums[r];
            while (curSum > x && l <= r)
                curSum -= nums[l++];
            if (curSum == x)
                ans = min(ans, n - (r - l + 1));
            r++;
        }
        return ans == INT_MAX ? -1 : ans;
    }
};

int main()
{
    vector<int> tmp{8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309};
    cout << Solution().minOperations(tmp, 134365) << endl;
}