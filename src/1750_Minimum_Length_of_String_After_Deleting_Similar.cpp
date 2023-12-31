#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumLength(string s) {
        int st = 0;
        int ed = s.size() - 1;
        while (st < ed && s[st] == s[ed])
        {
            while (st < ed && s[st] == s[st + 1])
                st++;
            st++;
            while (st < ed && s[ed] == s[ed - 1])
                ed--;
            ed--;
        }
        return max(0, ed - st + 1);
    }
};

int main()
{
    cout << Solution().minimumLength("ca") << endl;
}
