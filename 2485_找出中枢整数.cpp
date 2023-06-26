#include <bits/stdc++.h>
using namespace std;
int main() {

}
class Solution {
public:
    int pivotInteger(int n) {
        for (int i = 1; i <= n; ++i) {
            if ((1 + i) * i / 2 == (i + n) * (n - i + 1) / 2) {
                return i;
            }
        }
        return -1;
    }
};
