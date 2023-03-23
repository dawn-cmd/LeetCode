#include "bits/stdc++.h"
using namespace std;

class AuthenticationManager {
private:
    // timeToLive 存储令牌的有效时间（秒数）
    int timeToLive;
    // tokens 是一个字符串到 int 的映射，用于存储令牌到过期时间的映射
    unordered_map<string, int> tokens;

    // removeExpiredTokens 函数用于删除已经过期的令牌
    void removeExpiredTokens(int currentTime) {
        auto newEnd = std::remove_if(tokens.begin(), tokens.end(), 
            [currentTime](const auto& item) { return item.second <= currentTime; });
        tokens.erase(newEnd, tokens.end());
    }

public:
    // 构造函数，初始化 timeToLive
    AuthenticationManager(int timeToLive) : timeToLive(timeToLive) {}

    // generate 函数用于生成令牌
    void generate(string tokenId, int currentTime) {
        removeExpiredTokens(currentTime);
        tokens[tokenId] = currentTime + timeToLive;
    }    

    // renew 函数用于续期令牌
    void renew(string tokenId, int currentTime) {
        removeExpiredTokens(currentTime);
        auto it = tokens.find(tokenId);
        if (it == tokens.end()) {
            return;
        }
        it->second = currentTime + timeToLive;
    }    

    // countUnexpiredTokens 函数返回仍然未过期的令牌数
    int countUnexpiredTokens(int currentTime) {
        removeExpiredTokens(currentTime);
        return tokens.size();
    }
};
int main() {
    AuthenticationManager test(5);
    test.renew("aaa", 1);
    test.generate("aaa", 2);
    cout << test.countUnexpiredTokens(6) << '\n';
    test.generate("bbb", 7);
    test.renew("aaa", 8);
    test.renew("bbb", 10);
    cout << test.countUnexpiredTokens(15) << '\n';
}
