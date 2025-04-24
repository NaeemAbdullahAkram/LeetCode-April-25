class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_unique = len(set(nums))
        from collections import defaultdict
        freq = defaultdict(int)
        res = left = unique = 0

        for right, val in enumerate(nums):
            freq[val] += 1
            if freq[val] == 1:
                unique += 1
            while unique == total_unique:
                res += len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    unique -= 1
                left += 1
        return res