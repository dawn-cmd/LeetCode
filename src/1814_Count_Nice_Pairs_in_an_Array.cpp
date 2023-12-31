//
// Created by LightString on 1/17/2023.
//
#include "bits/stdc++.h"
using namespace std;
class Solution {
public:
    const int MOD = (int)(1e9 + 7);

    static int rev(int n) {
        int ans = 0;
        while (n)
        {
            ans = ans * 10 + n % 10;
            n /= 10;
        }
        return ans;
    }

    int countNicePairs(vector<int>& nums) {
        unordered_map<int, int> h;
        int ans = 0;
        for (int i = 0, tmp; i < nums.size(); ++i)
        {
            tmp = nums[i] - rev(nums[i]);
            ans = (ans + h[tmp]) % MOD;
            h[tmp]++;
        }
        return ans;
    }
};

int main() {
    vector<int> tmp{13, 10, 35, 24, 76};
    cout << Solution().countNicePairs(tmp) << endl;
}