# Q1) Given an array of distinct integers, find if there are two pairs (a, b) and (c, d) such that a+b = c+d, and a, b, c and d are distinct elements. If there are multiple answers, then print any of them. Expected complexity :  O(n2
import collections
input  = [3,4,7,1,2,9,8]

def solution(nums):
    hashset = set(nums)
    nums = list(hashset)
    hashmap = collections.defaultdict(list)
    for i in range(len(nums)):
        for j in range(i):
            s = nums[i]+nums[j]
            if s in hashmap:
                return ((nums[i],nums[j]),hashmap[s])
            hashmap[s] = ((nums[i]),nums[j])

print solution(input)