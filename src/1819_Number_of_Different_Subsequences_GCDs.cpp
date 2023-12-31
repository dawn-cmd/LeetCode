//
// Created by LightString on 1/14/2023.
//
#include "bits/stdc++.h"
using namespace std;
class Solution
{
public:
    int gcd(const int &a, const int &b)
    {
        return b ? gcd(b, min(a % b, a - b)) : a;
    }

    int countDifferentSubsequenceGCDs(vector<int>& nums)
    {
        int maxn = -1;
        for (const auto &num: nums)
            maxn = maxn > num ? maxn : num;
        int ans = 0;
        unordered_set<int> h(nums.begin(), nums.end());
        for (int i = 1, seqGCD; i <= maxn; ++i) {
            seqGCD = 0;
            for (int j = 1; j * i <= maxn; ++j)
            {
                if (h.count(j * i) == 0)
                    continue;
                seqGCD = seqGCD ? gcd(j, seqGCD) : j;
                if (seqGCD == 1)
                    break;
            }
            if (seqGCD == 1)
                ans++;
        }
        return ans;
    }
};

int main()
{
    vector<int> tmp{5,15,40,5,6};
    cout << Solution().countDifferentSubsequenceGCDs(tmp) << endl;
}