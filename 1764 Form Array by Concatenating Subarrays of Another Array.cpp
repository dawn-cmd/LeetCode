#include "bits/stdc++.h"
using namespace std;

class Solution {
public:
    bool canChoose(vector<vector<int>>& groups, vector<int>& nums) {
        int st = 0;
        int ed = 0;
        for (auto & group : groups)
        {
            bool is_find = false;
            while (st < nums.size() && ed < nums.size())
            {
                if (nums[ed] != group[ed - st])
                {
                    st += 1;
                    ed = st;
                    continue;
                }
                if (ed - st + 1 == group.size())
                {
                    st = ed + 1;
                    ed = st;
                    is_find = true;
                    break;
                }
                ed += 1;
            }
            if (!is_find)
                return false;
        }
        return true;
    }
};

int main()
{
    vector<vector<int>> g{{21,22,21,22,21,30}};
    vector<int> nums{21,22,21,22,21,22,21,30};
    cout << Solution().canChoose(g, nums) << endl;
}