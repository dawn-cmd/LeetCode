#include "bits/stdc++.h"
#include<immintrin.h>

using us = unsigned short;
const int N = 20005;
us a[N] __attribute__((aligned(32)));
#define _mm256_cmple_epi16(a, b) ((__m256i)((__v16hi)a<=(__v16hi)b))
#define _mm256_cmpge_epi16(a, b) ((__m256i)((__v16hi)a>=(__v16hi)b))
using namespace std;

class Solution{
public:
    __attribute__((no_sanitize_address, no_sanitize_memory))
    __attribute__((target("avx2")))
    int countPairs(vector<int> &_a, us l, us r) {
        int n = _a.size();
        int ans = 0;
        int d = 0;
        for (int i = 0; i < n; ++i)
            a[i] = _a[i];
        sort(a, a + n);
        __m256i L = _mm256_set1_epi16(l),
                R = _mm256_set1_epi16(r),
                mask = _mm256_set1_epi16(1);
        for (int i = 0; i < n; ++i)
        {
            if (i && a[i] == a[i - 1])
            {
                ans += d;
                continue;
            }
            us x = a[i];
            int j = i + 1;
            d = 0;
            __m256i X = _mm256_set1_epi16(x);
            __m256i res = _mm256_setzero_si256();
            for (; (j & 15) && j < n; ++j)
                d += (x ^ a[j]) >= l && (x ^ a[j]) <= r;
            if (j < n)
                for (__m256i *I = (__m256i *) (a + j), *end = (__m256i *) (a + (n & ~15)); I != end; ++I)
                {
                    __m256i Y = _mm256_xor_si256(X, *I);
                    res = _mm256_add_epi16(res, _mm256_and_si256(
                            _mm256_and_si256(_mm256_cmpge_epi16(Y, L), _mm256_cmple_epi16(Y, R)), mask));
                }
            for (int k = 0; k < 16; ++k)
                d += ((us *) &res)[k];
            for (j = max(j, n & ~15); j < n; ++j)
                d += (x ^ a[j]) >= l && (x ^ a[j]) <= r;
            ans += d;
        }
        return ans;
    }
};

int main() {
    vector<int> nums{9, 8, 4, 2, 1};
    cout << Solution().countPairs(nums, 5, 14) << endl;
}