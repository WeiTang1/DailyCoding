input = [100, 4, 200, 1, 3, 2]

def solution(input):
    input.sort()
    dp = [1] * len(input)
    for i in range(1,len(input)):
        if input[i]  == input[i-1]+1:
            dp[i] = dp[i-1]+1

    return max(dp)

print solution(input)


def longestConsecutive(self, nums):
    nset = set(nums)
    ans = 0
    for num in nums:
        if num - 1 not in nset:
            cur = num
            streak = 1
            while cur + 1 in nset:
                cur += 1
                streak += 1
            ans = max(streak, ans)
    return ans