nums2 = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]


def maxValueSubArray(nums,k):
    arr = []
    result = []
    for index in range(k):

        if not arr:
            arr.append(index)
        elif nums[index] < nums[arr[-1]]:
            arr.append(index)
        else:
            while(len(arr) >0 and nums[arr[-1]]<=nums[index]):
                arr = arr[:-1]
            arr.append(index)
    for index in range(k,len(nums)):
        result.append(nums[arr[0]])
        while(len(arr)>0 and index-arr[0] >= k):
            arr = arr[1:]
        if not arr:
            arr.append(index)
        elif nums[index] < nums[arr[-1]]:
            arr.append(index)
        else:
            while(len(arr) >0 and nums[arr[-1]]<=nums[index]):
                arr = arr[:-1]
            arr.append(index)
    result.append(nums[arr[0]])
    print result

nums1 = [2, 5, -1, 7, -3, -1, -2]

def maxDifferenctSubArray(nums1,k):
    maxarray = []
    minarray = []
    result = []
    for index in range(k):
        while len(maxarray)>0 and nums1[maxarray[-1]]<=nums1[index]:
            maxarray = maxarray[:-1]

        maxarray.append(index)

        while len(minarray)>0 and nums1[minarray[-1]]>=nums1[index]:
            minarray = minarray[:-1]
        minarray.append(index)
    print minarray
    print maxarray
    for index in range(k,len(nums1)):
        result.append(nums1[maxarray[0]]+nums1[minarray[0]])

        while len(maxarray)>0 and index - maxarray[0]>=k :
            maxarray = maxarray[1:]

        while len(minarray)>0 and index - minarray[0]>=k :
            minarray = minarray[1:]

        while len(maxarray)>0 and nums1[maxarray[-1]]<=nums1[index]:
            maxarray = maxarray[:-1]
        maxarray.append(index)

        while len(minarray)>0 and nums1[minarray[-1]]>=nums1[index]:
            minarray = minarray[:-1]
        minarray.append(index)
        print minarray
        print maxarray

    result.append(nums1[maxarray[0]] + nums1[minarray[0]])
    print result


maxDifferenctSubArray(nums1,4);