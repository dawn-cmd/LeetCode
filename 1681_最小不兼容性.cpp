#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minimumIncompatibility(vector<int>& nums, int k) {
        unordered_map<int, int> val;
        int n = nums.size();
        int group_size = n / k;
        for (int cur = 1; cur < (1 << n); ++cur) {
            if (bitset<32>(cur).count() != group_size) continue;
            
        }
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
}
