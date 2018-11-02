def permute (nums):
    li = []
    for i in nums:
        helper(li,[i],nums)
    print li
    return list

def helper(li,permutation,nums):
    if len(permutation) == len(nums):
        li.append(permutation)
        print permutation
        return
    for i in nums:
        if i in permutation:
            continue
            permutation.append[i]
            helper(li,permutation,nums)
            permutation.pop()

permute([1,2,3]);