#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        for (int i = 0; i < nums.size(); ++i) {
            while (1 <= nums[i] && nums[i] - 1 < nums.size() && nums[i] - 1 != i && nums[i] != nums[nums[i] - 1]) {
                swap(nums[i], nums[nums[i] - 1]);
            }
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (i + 1 != nums[i]) {
                return i + 1;
            }
        }
        return nums.size() + 1;
    }
};
