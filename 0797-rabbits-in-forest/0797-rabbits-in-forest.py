class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers) # {1:2, 2:1} #{key(number): value(count of number)}
        ans = 0
        for k in freq:
            group_size = k+1
            groups = ceil(freq[k]/group_size)
            ans += groups*group_size
        return ans 
            