def dfs(nums,path,all):
    if not nums:
        all.append(path)
    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:],path+[nums[i]],all)

def permutation(nums):
    set = []
    dfs(nums,[],set)
    print set


def permutation2(nums):
    if len(nums) == 1:
        return [nums]
    r = []
    for i, num in enumerate(nums):
        newnums = nums[:i]+nums[i+1:]
        for s in permutation2(newnums):
            r.append([num]+s)
    return r

# permutation([1,2,3])
print permutation2([1,2,3])
