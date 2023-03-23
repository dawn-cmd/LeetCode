//
// Created by LightString on 1/5/2023.
//
#include "bits/stdc++.h"
using namespace std;

class Solution {
public:
    static int countDigit(int n)
    {
        int ans = 0;
        while (n)
        {
            ans += n % 10;
            n /= 10;
        }
        return ans;
    }

    int countEven(int num) {
        int ans = 0;
        for (int i = 1; i <= num; ++i)
            if (!(countDigit(i) & 1))
                ans++;
        return ans;
    }
};

int main() {
    Solution sol;

    // Test countEven method with various input values
    cout << sol.countEven(10) << endl;
    assert(sol.countEven(10) == 4);
    assert(sol.countEven(20) == 8);
    assert(sol.countEven(30) == 14);
    assert(sol.countEven(40) == 21);
    assert(sol.countEven(50) == 28);

    cout << "All tests passed!" << endl;
    return 0;
}
