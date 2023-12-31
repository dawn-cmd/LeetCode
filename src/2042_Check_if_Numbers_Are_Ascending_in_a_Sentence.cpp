//
// Created by LightString on 1/3/2023.
//

#include "bits/stdc++.h"
using namespace std;

class Solution{
public:

    static int getNum(const string& s, int &id)
    {
        while (id < s.size() && !isdigit(s[id]))
            id += 1;
        int num = 0;
        while (id < s.size() && isdigit(s[id]))
            num = num * 10 + (s[id++] - '0');
        return num;
    }

    bool areNumbersAscending(string s) {
        int prev = 0;
        int id = 0;
        int cur = getNum(s, id);
        while (cur)
        {
            if (cur <= prev)
                return false;
            prev = cur;
            cur = getNum(s, id);
        }
        return true;
    }
};

int main()
{
    cout << Solution().areNumbersAscending("hello world 5 x 3") << endl;
}