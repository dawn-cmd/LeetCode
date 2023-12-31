#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    string bestHand(const vector<int>& ranks, const vector<char>& suits) {
        unordered_set<char> s;  // 用于统计牌的花色种类的集合
        for(char suit : suits){
            s.emplace(suit);  // 将花色加入集合中
        }
        if(s.size() == 1)  // 如果集合中只有一种花色，则为同花
            return "Flush";

        unordered_map<int,int> cntrank;  // 用于统计每种数字牌的数量的哈希表
        for(int rank : ranks){
            cntrank[rank]++;  // 将每张牌的数字加入哈希表，并统计每种数字牌的数量
        }
        if(cntrank.size() == 5)  // 如果哈希表中的键值对数量为 5，则为高牌
            return "High Card";
        for(auto ra : cntrank){  // 遍历哈希表
            if(ra.second > 2)  // 如果有三张或以上相同数字的牌，则为三条
                return "Three of a Kind";
        }
        return "Pair";  // 否则为对子
    }
};
