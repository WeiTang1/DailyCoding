input = [0,1,2,3,4,5,6,7,8]
input2 = 13

def printt(arr,lo,hi):
    print "------"
    for i in range(len(arr)):
        print arr[i],
    print
    for i in range(len(arr)):
        if i == lo or i == hi:
            print "^",
        else:
            print " ",
    print

def tempalteOne(nums,target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        printt(nums,lo,hi)
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def templateTwo(nums,target):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        printt(nums,lo,hi)
        mid = lo + (hi - lo) // 2
        print mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    if nums[lo] == target:
        return lo
    if nums[hi] == target:
        return hi
    else:
        return -1

print templateTwo(input,7)
