//
// Created by LightString on 1/18/2023.
//
#include "bits/stdc++.h"
using namespace std;
class Solution {
private:
    static bool checkLowerCase(const string &password) {
        return any_of(password.begin(),
                      password.end(),
                      [](const auto &c){return 'a' <= c && c <= 'z';});
    }
    static bool checkUpperCase(const string &password) {
        return any_of(password.begin(),
                      password.end(),
                      [](const auto &c){return 'A' <= c && c <= 'Z';});
    }
    static bool checkDigit(const string &password) {
        return any_of(password.begin(),
                      password.end(),
                      [](const auto &c){return '0' <= c && c <= '9';});
    }
    static bool checkSpecialCharacter(const string &password) {
        unordered_set<char> h{'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+'};
        return any_of(password.begin(),
                      password.end(),
                      [&h](const auto &c){return h.find(c) != h.end();});
    }
public:
    static bool strongPasswordCheckerII(string password) {
        if (password.size() < 8)  // check length
            return false;
        for (int i = 0; i < password.size() - 1; ++i)  // check duplicated
            if (password[i] == password[i + 1])
                return false;
        return checkLowerCase(password) &&
               checkUpperCase(password) &&
               checkDigit(password) &&
               checkSpecialCharacter(password);
    }
};

int main() {

}