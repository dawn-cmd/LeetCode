#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoOutOfThree(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3) {
        unordered_map<int, int> h;
        unordered_set<int> s1(nums1.begin(), nums1.end());
        unordered_set<int> s2(nums2.begin(), nums2.end());
        unordered_set<int> s3(nums3.begin(), nums3.end());
        for (const auto& num: s1)
            h[num] += 1;
        for (const auto& num: s2)
            h[num] += 1;
        for (const auto& num: s3)
            h[num] += 1;
        vector<int> ans;
        for (const auto& item: h)
            if (item.second >= 2)
                ans.push_back(item.first);
        return ans;
    }
};

int main() 
{ 
    Solution solution; 
    vector nums1 = {1, 2, 3}; 
    vector nums2 = {2, 3, 4}; 
    vector nums3 = {3, 4, 5}; 
    vector ans = solution.twoOutOfThree(nums1, nums2, nums3); 
    for (auto num : ans) 
    { 
        cout << num << " "; 
    } 
    cout << endl; 
    return 0; 
}
