class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arraySum = sum(nums)
        if arraySum % 2 != 0:
            return False
        
        target = arraySum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
            if dp[target]:
                break
            
        return dp[target]        