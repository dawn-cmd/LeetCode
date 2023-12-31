//
// Created by LightString on 1/17/2023.
//
#include "bits/stdc++.h"
using namespace std;
class MKAverage {
private:
    int m;
    int k;
    long long sum;
    queue<int> q;
    map<int, int> h;
public:
    MKAverage(int m, int k) {
        this->m = m;
        this->k = k;
        sum = 0;
    }
    void addElement(int num) {
        q.emplace(num);
        h[num]++;
        sum += num;
        while (q.size() > m)
        {
            h[q.front()]--;
            sum -= q.front();
            q.pop();
        }
    }
    int calculateMKAverage() {
        while (q.size() < m)
            return -1;
        long long tmp = sum;
        int tmpCnt = 0;
        for (auto &i : h)
        {
            if (tmpCnt == k)
                break;
            tmp -= i.first * min(i.second, k - tmpCnt);
            tmpCnt += min(i.second, k - tmpCnt);
        }
        tmpCnt = 0;
        for (auto i = h.rbegin(); i != h.rend(); ++i)
        {
            if (tmpCnt == k)
                break;
            tmp -= i->first * min(i->second, k - tmpCnt);
            tmpCnt += min(i->second, k - tmpCnt);
        }
        return (int)(tmp / (m - (k << 1)));
    }
};

int main() {

}