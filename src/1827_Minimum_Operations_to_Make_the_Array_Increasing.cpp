#include <bits/stdc++.h>
#define max(a, b) a > b ? a : b
using namespace std;

class Solution
{
public:
    int minOperations(vector<int>& nums)
    {
        int ans = 0;
        for (int i = 1; i < nums.size(); ++i)
        {
            ans += max(nums[i - 1] + 1 - nums[i], 0);
            nums[i] = max(nums[i], nums[i - 1] + 1);
        }
        return ans;
    }
};

int main()
{
    vector<int> tmp {1, 1, 1};
    cout << Solution().minOperations(tmp) << endl;
}