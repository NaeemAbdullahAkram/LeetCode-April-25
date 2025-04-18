class Solution:
    MAX_N = 30
    
    @staticmethod
    def say(s):
        c = s[0]
        start = 0
        result = ""
        for i in range(len(s) + 1):
            if i == len(s) or s[i] != c:
                result += str(i - start)
                result += c
                if i != len(s):
                    c = s[i]
                    start = i
        return result
    
    def countAndSay(self, n: int) -> str:
        return Solution.answers[n - 1]


def calculate():
    result = ["1"]
    for i in range(2, Solution.MAX_N + 1):
        result.append(Solution.say(result[-1]))
    return result

Solution.answers = calculate()