class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> countArray;
        for (int i = 0; i < nums.size(); i++){
            countArray[nums[i]]++;
            if(countArray[nums[i]] > 1){
                return true;
            }
        }
        return false;
    }
};