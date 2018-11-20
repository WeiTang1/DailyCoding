def dfs(nums,path,all):
    if not nums:
        all.append(path)
    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:],path+[nums[i]],all)

def permutation(nums):
    set = []
    dfs(nums,[],set)
    print set


permutation([1,2,3])
