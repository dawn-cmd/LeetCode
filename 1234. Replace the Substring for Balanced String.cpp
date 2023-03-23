#include "bits/stdc++.h"
using namespace std;
// Solution class to find a balanced String
class Solution {
public:
    // Function to return the minimum length of a balanced string
    int balancedString(const string &s) {
        // Map to track the occurences of characters in string s
        unordered_map<char, int> nums{{'Q', 0}, {'W', 0}, {'E', 0}, {'R', 0}};
        // Updating the number of occurences in map
        for (const auto &c: s) {
            nums[c]++;
        }
        // Updating the map values with the difference of number of characters required
        for (const auto &c: {'Q', 'W', 'E', 'R'}) {
            nums[c] -= s.size() / 4;
        }
        // Initializing the answer
        int ans = 0x3f3f3f3f;
        // Start index for the substring under evaluation
        int j = -1;
        // Iterating through every character in the input string
        for (int i = 0; i < s.size(); i++) {
            // Iterating from j + 1 to the end of string
            while (nums['Q'] > 0 || nums['W'] > 0 || nums['E'] > 0 || nums['R'] > 0) {
                if (j == s.size() - 1) {
                    break;
                }
                // Using character at j + 1
                nums[s[++j]]--;
            }
            // Checking if there exists such a substring
            if (nums['Q'] <= 0 && nums['W'] <= 0 && nums['E'] <= 0 && nums['R'] <= 0) {
                ans = min(ans, j - i + 1);
            }
            // Reevaluating by adding character at index i
            nums[s[i]]++;
        }
        // Returning minimum balanced substring length
        return ans;
    }
};
int main() {
    cout << Solution().balancedString("QQQW") << endl;
}
