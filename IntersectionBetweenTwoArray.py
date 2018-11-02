
A = [(1, 2), (3, 4), (7, 10)]
B = [(0, 2), (3, 8), (9, 12)]

def intersection(interval1, interval2):
    if interval1 is None or interval2 is None:
        return None
    left1,right1 = interval1
    left2,right2 = interval2
    rightmostleft = max(left1, left2)
    leftmostright = min(right1, right2)
    if rightmostleft>leftmostright:
        return None
    return rightmostleft,leftmostright


#solution 1 O(n^2) but this didn't really use the essence of sorted non-over lapping array
def findintersection(array1, array2):
    if array1 is None or array2 is None:
        return None
    result = []
    for interval1 in array1:
        for interval2 in array2:
            inter = intersection(interval1,interval2);
            if inter is not None:
                result.append(inter);
    return result;

#solution 2
#O(n)
def findinterseciont2(array1, array2):
    if array1 is None or array2 is None:
        return None
    i, j, result = 0, 0, [];
    while i<len(array1) and j<len(array2):
        inter = intersection(array1[i], array2[j])
        if inter is not None :
            result.append(inter)
        if(array2[j][1]>array1[i][1]):
            i += 1
        elif(array2[j][1]<array1[i][1]):
            j += 1
        else:
            i+=1
            j+=1
    return result;
#
#
# print findintersection(A,B)
#
# print findinterseciont2(A,B)
