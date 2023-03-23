#include "bits/stdc++.h"
using namespace std;
class Solution {
public:
    string printBin(double num) {
        double cur = 1;
        stringstream ans;
        ans << "0.";
        for (int i = 0; i < 30; ++i) {
            if (num == 0) {
                return ans.str();
            }
            cur /= 2;
            ans << (num >= cur ? '1' : '0');
            num = (num >= cur) ? (num - cur) : (num);
        }
        return "ERROR";
    }
};
int main() {
    cout << Solution().printBin(0.1) << '\n';
}
