#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool isNumber(string s) {
        string rule_float("[+-]?(\\d+\\.\\d+|\\d+\\.|\\.\\d+)");
        string rule_int("[+-]?\\d+");
        regex rule_num("(" + rule_float + "|" + rule_int + ")([eE]" + rule_int + ")?"); 
        return regex_match(s, rule_num);
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout << Solution().isNumber("") << '\n';
}
