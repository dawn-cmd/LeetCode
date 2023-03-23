#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
using namespace std;

class Solution 
{
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) 
    {
        int ans = -1;
        int mind = INF;
        for (int i = 0; i < points.size(); ++i)
        {
            if (points[i][0] != x && points[i][1] != y)
                continue;
            if (abs(x - points[i][0]) + abs(y - points[i][1]) < mind)
            {
                ans = i;
                mind = (int)(abs(x - points[i][0]) + abs(y - points[i][1]));
            }
        }
        return ans;
    }
};
