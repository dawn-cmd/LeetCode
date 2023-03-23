// Program to find the names of security personnel who 
// pressed the alarm button more than three times during a 1-hour window.

#include <bits/stdc++.h>

// TIME_SINGLE is used to convert minutes to seconds.
const int TIME_SINGLE = 60;

class Solution {
public:
    // The function 'alertNames' returns a vector of strings containing names
    // of the security personnel who pressed the alarm button more than
    // three times in one hour. 
    
    std::vector<std::string> alertNames(std::vector<std::string>& keyName, std::vector<std::string>& keyTime) {
        // 'getTime' is a lambda function used to convert the time from string format (e.g. "11:00")
        // to a number representing the minutes from midnight (e.g. 660).
        auto getTime = [] (std::string t) {
            return std::stoi(t.substr(0, 2)) * TIME_SINGLE + std::stoi(t.substr(3, 2));
        };
        
        // 'key' is a vector of pairs, where each pair contains the minutes
        // from midnight (a integer) and the name of the security personnel
        // who pressed the alarm button.
        std::vector<std::pair<int, std::string>> key;
        for (int i = 0; i < keyName.size(); ++i) {
            key.emplace_back(getTime(keyTime[i]), keyName[i]);
        }
        
        // The vector 'key' is sorted based on time-from-midnight.
        std::sort(key.begin(), key.end());
        
        // 'record' is a map whose keys are names of security personnel and values
        // are vectors representing the times they pressed the alarm button.
        std::map<std::string, std::vector<int>> record;
        
        // 'alarm' is a set of names of security personnel who pressed
        // the alarm button more than three times in an hour.
        std::set<std::string> alarm;
        
        for (int i = 0; i < key.size(); ++i) {
            // Add a time to the corresponding security personnel's record.
            record[key[i].second].push_back(key[i].first);
            
            // If a security personnel has pressed the alarm button less than three times,
            // skip the rest of this iteration and start the next iteration.
            if (record[key[i].second].size() < 3) {
                continue;
            }
            
            // If a security personnel has pressed the alarm button more than three times within
            // an hour, add the name to set 'alarm'.
            if (key[i].first - record[key[i].second][record[key[i].second].size() - 3] <= TIME_SINGLE) {
                alarm.emplace(key[i].second);
            }
        }
        
        // Convert set 'alarm' to vector 'ans'.
        std::vector<std::string> ans(alarm.begin(), alarm.end());
        
        return ans;
    }
};

int main() {
    // Test inputs.
    std::vector<std::string> name{"daniel","daniel","daniel","luis","luis","luis","luis"};
    std::vector<std::string> time{"10:00","10:40","11:00","09:00","11:00","13:00","15:00"};

    // Get results.
    std::vector<std::string> ans;
    ans = Solution().alertNames(name, time);
    
    // Output results.
    for (const auto &item : ans) {
        std::cout << item << '\n';
    }
}
