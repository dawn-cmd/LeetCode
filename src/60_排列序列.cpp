#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> factorial(n);
        factorial[0] = 1;
        for (int i = 1; i < n; ++i) factorial[i] = factorial[i - 1] * i;
        string ans = "";
        k--;
        for (int i = 1; i <= n; ++i) {
            int order = k / factorial[n - i] + 1;
            
        }
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout << Solution().getPermutation(4, 9) << '\n';
}

