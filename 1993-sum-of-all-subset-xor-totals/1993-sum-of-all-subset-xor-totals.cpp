class Solution {
public:

    int subsetXORSum(vector<int>& nums) {
        int bitwiseOrOfAll = 0;

        for (int num : nums) {
            bitwiseOrOfAll |= num;
        }
        return bitwiseOrOfAll << (nums.size() - 1);
        // 2^{n - 1} * bitwiseOrOfAll
    }
};