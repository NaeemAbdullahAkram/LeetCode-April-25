class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        indices = defaultdict(list)

        for i, ele in enumerate(nums):
            indices[ele].append(i)
        
        count = 0
        for v in indices.values():
            len_v = len(v)
            for i in range(len_v-1):
                if v[i] % k == 0:
                    count += len_v - i - 1
                    continue
                for j in range(i+1,len_v):
                    if (v[i] * v[j]) % k == 0:
                        count += 1
        return count
        