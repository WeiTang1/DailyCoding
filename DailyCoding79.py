input1 = [10, 5, 7]
input3 = [1,2,3,4,5,6,7,8,9,11,10,12]
input2 = [10,5,1]

def solution(nums):
    found = False
    for i in range(1,len(nums)):
        if nums[i]<nums[i-1]:
            if found:
                return False
            else:
                found = True
    return True

print solution(input3)