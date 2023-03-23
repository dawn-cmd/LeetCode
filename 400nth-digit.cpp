#include <bits/stdc++.h>
using namespace std;
class Solution {
    public:
        int findNthDigit(int n) {
            if (n < 10) {
                return n;
            }
            // Calculate the number of digits
            long long len = 1;
            while (n > len * 9 * pow(10, len - 1)) {
                n -= len * 9 * pow(10, len - 1); 
                len++;
            }
            // Get the specific digit
            long long num = (n + 1) / len + pow(10, len - 1) - 1;
            long long nch = n % len ? n % len : len;
            long long tmpa = pow(10, len - nch);
            long long tmpb = pow(10, len - nch + 1);
            return num % tmpb / tmpa;
        }
};
int main() {
    Solution solution;
    int n;
    cin >> n;
    cout << solution.findNthDigit(n) << endl;
    return 0;
}