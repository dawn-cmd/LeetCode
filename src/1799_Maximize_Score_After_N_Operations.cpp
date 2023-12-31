#include "bits/stdc++.h"
using namespace std;
class Solution {
public:
    int gcd(int a, int b)
    {
        if (a < b)
            swap(a, b);
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }

    int getId(vector<int>& cur)
    {
        int ans = 0;
        for (int i = 0; i < cur.size(); ++i)
            ans = ans * 2 + cur[i];
        return ans;
    }

    int count(vector<int>& his, vector<int>& nums, vector<int>& cur, int lv)
    {
        if (lv == 0)
            return 0;
        int id = getId(cur);
        if (his[id] != -1)
            return his[id];
        int n = cur.size();
        int ans = 0;
        for (int i = 0; i < n - 1; ++i)
            for (int j = i + 1; j < n; ++j)
            {
                if (cur[i] == 0 || cur[j] == 0)
                    continue;
                cur[i] = 0;
                cur[j] = 0;
                ans = max(ans, gcd(nums[i], nums[j]) * lv + count(his, nums, cur, lv - 1));
                cur[i] = 1;
                cur[j] = 1;
            }
        his[id] = ans;
        return ans;
    }

    int maxScore(vector<int>& nums)
    {
        int n = nums.size();
        vector<int> his(pow(2, n));
        for (int i = 0; i < pow(2, n); ++i)
            his[i] = -1;
        vector<int> cur(n);
        for (int i = 0; i < n; ++i)
            cur[i] = 1;
        return count(his, nums, cur, n / 2);
    }
};

int main()
{
    vector<int> nums{1, 2, 3, 4, 5, 6};
    cout << Solution().maxScore(nums) << endl;
}