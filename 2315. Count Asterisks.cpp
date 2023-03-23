#include "bits/stdc++.h"
using namespace std;
class Solution {
public:
    int countAsterisks(const string &s) {
        int isPaired = 0;
        int cnt = 0;
        for (const auto &c : s) {
            if (c == '|') {
                isPaired ^= 1;
                continue;
            }
            if (c == '*' && !isPaired) ++cnt;
        }
        return cnt;
    }
};
int main() {
    cout << Solution().countAsterisks("l|*e*et|c**o|*de|") << '\n';
}
