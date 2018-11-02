schedule = [(30, 75), (0, 50), (60, 150)]
schedule2 = [(1,5),(4,6),(0,8)]

def mergesort(array):
    if(len(array)>1):
        mid = len(array)//2

        leftarray = array[:mid]
        rightarray = array[mid:]
        mergesort(leftarray)
        mergesort(rightarray)
        #merge
        i,j,k = 0,0,0
        while i < len(leftarray) and j < len(rightarray):
            if leftarray[i][0] < rightarray[j][0]:
                array[k] = leftarray[i]
                i+=1
            else:
                array[k] = rightarray[j]
                j+=1
            k+=1
        while i < len(leftarray):
            array[k] = leftarray[i]
            i+=1
            k+=1
        while j < len(rightarray):
            array[k] = rightarray[j]
            j+=1
            k+=1



# O(n^2) time
def numOfRoom(schedule):
    if (len(schedule) < 1):
        return 1
    mergesort(schedule)
    room = []
    print schedule
    room.append(schedule[0][1])
    for i in range(1,len(schedule)):
        found = False
        for index, r in enumerate(room):
            print r ,"vs", schedule[i][0]
            if(schedule[i][0]>= r):
                room[index] = schedule[i][1]
                found = True
                break
        if not found:
            room.append(schedule[i][1])

        print room
    return len(room)

def intersect(class1,class2):
    if(class1[0]>class2[1] or class2[0]>class1[1]):
        return False
    return True

print numOfRoom(schedule2)
