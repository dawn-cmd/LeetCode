#include "bits/stdc++.h"
using namespace std;
class Solution {
public:
    int minMaxGame(vector<int>& nums) {
        while (nums.size() > 1)
        {
            for (int i = 0; i < (nums.size() >> 1); ++i)
                nums[i] = (i & 1)
                    ? max(nums[(i << 1)], nums[(i << 1) | 1])
                    : min(nums[(i << 1)], nums[(i << 1) | 1]);
            nums.resize(nums.size() >> 1);
        }
        return nums[0];
    }
};

int main()
{

}