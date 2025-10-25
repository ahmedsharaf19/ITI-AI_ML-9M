// Problem Link: https://leetcode.com/problems/valid-anagram/
// Submission Link: https://leetcode.com/problems/valid-anagram/submissions/1806738817/

#include <string>
using namespace std;
bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;
        int countingChar[26] = {0};
        for(int i = 0; i < s.size(); i++){
            countingChar[s[i] - 97]++;
        }
        for(int i = 0; i < t.size(); i++){
            if(countingChar[t[i] - 97] <= 0){
                return false;
            }
            countingChar[t[i] - 97]--;
            
        }
        return true;
}