#include <bits/stdc++.h> // Includes all standard library
using namespace std;

// Define Solution class
class Solution {
public:
    // Function to calculate minimum incompatibility
    int minimumIncompatibility(vector<int>& nums, int k) {
        unordered_map<int, int> val; // Map to store all possible subsets of nums and their incompatibility
        int n = nums.size(); // Store size of nums
        int group_size = n / k; // Size of each group

        // Calculate incompatibility for all subsets of nums
        for (int cur = 1; cur < (1 << n); ++cur) { // Loop over all subsets of nums
            if (bitset<32>(cur).count() != group_size) continue; // If current subset does not have group_size elements, skip
            int minn = 0x3f3f3f3f; // Initialize minimum
            int maxn = -0x3f3f3f3f; // Initialize maximum
            unordered_set<int> vis; // Set to store all unique elements of current subset
            
            // Calculate minn and maxn of current subset
            for (int i = 0; i < n; ++i) { 
                if (!((1 << i) & cur)) continue; // If ith element is not in current subset, skip
                if (vis.count(nums[i])) break; // If ith element is already in set, break
                vis.insert(nums[i]); // Insert ith element in set
                minn = min(minn, nums[i]); // Update minn
                maxn = max(maxn, nums[i]); // Update maxn
            }
            if (vis.size() != group_size) continue; // If current subset does not have group_size elements, skip
            val[cur] = maxn - minn; // Store incompatibility of current subset in val
        }
        
        // Dynamic Programming to find minimum incompatibility
        vector<int> dp(1 << (n + 1), 0x3f3f3f3f); // Initialize dp array with large number
        dp[0] = 0; // dp[0] = 0
        
        // Calculate dp values
        for (int cur = 0; cur < (1 << n); ++cur) {
            if (dp[cur] == 0x3f3f3f3f) continue; // If dp[cur] is not calculated, skip
            unordered_map<int, int> space; // Map to store all unchosen elements and their positions
            
            // Initialize space
            for (int i = 0; i < n; ++i) {
                if ((1 << i) & cur) continue; // If ith element is already chosen, skip
                space[nums[i]] = i; // Store position of ith element in space
            }
            if (space.size() < group_size) continue; // If number of unchosen elements is less than group_size, skip
            int sub = 0; 
            
            // Calculate sub
            for (const auto &item: space) sub |= 1 << item.second; 
            
            // Calculate dp values
            for (int tmp = sub; tmp; tmp = (tmp - 1) & sub) {
                if (val.find(tmp) == val.end()) continue; // If tmp is not in val, skip
                dp[cur | tmp] = min(dp[cur | tmp], dp[cur] + val[tmp]); // Update dp[cur | tmp]
            }
        }
        
        // If dp[(1 << n) - 1] is not calculated, return -1, else return dp[(1 << n) - 1]
        return dp[(1 << n) - 1] == 0x3f3f3f3f ? -1 : dp[(1 << n) - 1];
    }
};

// Main function
int main() {
    ios::sync_with_stdio(0); // Fast IO
    cin.tie(0); // Untie cin and cout
    vector<int> tmp{6,8,5,16,8,12,11,7,13,16,15,14,7,9,1,10}; // Test input
    cout << Solution().minimumIncompatibility(tmp, 4); // Call minimumIncompatibility function and print result
}
