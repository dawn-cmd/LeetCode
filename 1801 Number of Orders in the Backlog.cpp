#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL MOD = (LL)(1000000007);

class Solution {
public:
    static void addBuyOrder(LL price,
                            LL amount,
                            priority_queue<pair<LL, LL>, vector<pair<LL, LL>>, greater<>> &sellOrders,
                            priority_queue<pair<LL, LL>> &buyOrders
                            )
    {
        while (amount && !sellOrders.empty())  // there are still orders remain
        {
            if (sellOrders.top().first > price)  // if the smallest sell order is larger than this one, quit
                break;
            LL sellPrice = sellOrders.top().first;
            LL sellAmount = sellOrders.top().second;
            sellOrders.pop();
            if (amount >= sellAmount)
            {
                amount -= sellAmount;
                continue;
            }
            sellAmount -= amount;
            amount = 0;
            sellOrders.emplace(sellPrice, sellAmount);
        }
        if (amount)
            buyOrders.emplace(price, amount);
    }

    static void addSellOrder(LL price,
                      LL amount,
                      priority_queue<pair<LL, LL>, vector<pair<LL, LL>>, greater<>> &sellOrders,
                      priority_queue<pair<LL, LL>> &buyOrders
                      )
    {
        while (amount && !buyOrders.empty())
        {
            if (buyOrders.top().first < price)
                break;
            LL buyPrice = buyOrders.top().first;
            LL buyAmount = buyOrders.top().second;
            buyOrders.pop();
            if (amount >= buyAmount)
            {
                amount -= buyAmount;
                continue;
            }
            buyAmount -= amount;
            amount = 0;
            buyOrders.emplace(buyPrice, buyAmount);
        }
        if (amount)
            sellOrders.emplace(price, amount);
    }

    int getNumberOfBacklogOrders(vector<vector<int>>& orders) {
        priority_queue<pair<LL, LL>, vector<pair<LL, LL>>, greater<>> sellOrders;
        priority_queue<pair<LL, LL>> buyOrders;
        for (const auto &order: orders)
        {
            if (order[2] == 0)  // if it is a buy order
            {
                addBuyOrder(order[0], order[1], sellOrders, buyOrders);
                continue;
            }
            // if it is a sell order
            addSellOrder(order[0], order[1], sellOrders, buyOrders);
        }
        LL ans = 0;
        while (!buyOrders.empty())
        {
            ans = (ans + buyOrders.top().second) % MOD;
            buyOrders.pop();
        }
        while (!sellOrders.empty())
        {
            ans = (ans + sellOrders.top().second) % MOD;
            sellOrders.pop();
        }
        return (int)ans;
    }
};

int main() 
{
    vector<vector<int>> test = {{10, 5, 10}, {15, 2, 1}, {25, 1, 1}, {30, 4, 0}};
    cout << Solution().getNumberOfBacklogOrders(test) << endl;
}