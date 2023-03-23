#include <bits/stdc++.h>
using LL = long long;
using namespace std;

class Solution {
public:
    char repeatedCharacter(string s) {
        unordered_map<char, int> h;
        for (const auto &c: s)
        {
            if (h.count(c))
                return c;
            h[c] = 1;
        }
        return '?';
    }
};

int main() 
{ 
    Solution sol; string s1 = "abcde"; string s2 = "aabbccddee";
    cout << sol.repeatedCharacter(s1) << endl;
    cout << sol.repeatedCharacter(s2) << endl;
    return 0;
}
