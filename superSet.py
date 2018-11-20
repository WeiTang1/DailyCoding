numsset = [1,2]

def subset1(set):
    result = [[]]
    for i in set:
        result += [r + [i]for r in result]
    return result


def dfs(nums,index,path,re):
    re.append(path)
    for i in xrange(index,len(nums)):
        dfs(nums, i+1,path+[nums[i]],re)

def subset2(nums):
    re = []
    dfs(nums,0,[],re)
    return re


def subset3(nums):
    if nums == []:
        return [[]]
    result = []
    for index in range(len(nums)):
        newset = nums[index+1:]
        for sub in subset3(newset):
            if sub not in result:
                result.append(sub)
                result.append([nums[index]]+sub)
    return result

re = subset3(numsset)
print re