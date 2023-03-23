//
// Created by LightString on 1/9/2023.
//
#include "bits/stdc++.h"
using namespace std;

class Solution
{
public:
    int reinitializePermutation(int n) noexcept
    {
        int ans = 0;
        int id = 1;
        do
        {
            id = (id & 1) ? (n >> 1) + ((id - 1) >> 1) : (id >> 1);
            ans++;
        }
        while (id != 1);
        return ans;
    }
};

int main()
{
    printf("%d\n", Solution().reinitializePermutation(10));
}