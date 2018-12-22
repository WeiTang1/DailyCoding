input = [13, 18, 25, 2, 8, 10]


def solution(nums,target):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        elif nums[mid] < nums[hi]:
            hi = mid
        else:
            hi = hi - 1
    rotate = lo

    lo,hi = 0, len(nums)-1
    while lo <= hi:
        mid = lo+(hi-lo)//2
        _mid = (mid + rotate)%len(nums)

        if nums[_mid] == target:
            return _mid
        if nums[_mid] > target:
            hi = mid -1
        else:
            lo = mid +1
    return -1

print solution(input, 2)