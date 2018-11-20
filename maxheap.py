class heap:
    def  __init__(self):
        self.arr = []

    def insert(self,i):
        self.arr.append(i)
        pos = len(self.arr)-1
        while pos>0 and self.arr[pos]>self.arr[pos/2]:
            self.arr[pos],self.arr[pos/2] = self.arr[pos/2],self.arr[pos]
            pos = pos/2
        # while pos>0 and i> self.arr[pos/2]:
        #     self.arr[pos] = self.arr[pos/2]
        #     pos = pos/2
        # self.arr[pos] = i

    def __str__(self):
        str1 = ""
        for i in self.arr:
            str1 = str1 + str(i)+ " "
        return str1


    def heapsort(self):
        for n in range(len(self.arr)-1,-1,-1):
            self.arr[0], self.arr[n] = self.arr[n], self.arr[0]
            self.prelocate(0,n)

    def prelocate(self,i,n):
        while (2*i)+1 < n:
            idx, left, right = i, 2*i+1, 2*i+2

            if self.arr[left] > self.arr[right]:
                idx = left
            if right < n and self.arr[right] > self.arr[left]:
                idx = right
            if idx == i:
                return
            self.arr[idx],self.arr[i] = self.arr[i],self.arr[idx]
            i = idx

    def delete(self):
        top = self.arr[0]
        self.arr[0] = self.arr[len(self.arr)-1]
        self.arr.pop()
        self.prelocate(0,len(self.arr))
        return top

list = heap()

for i in range(10):
    list.insert(i)

print list
list.delete()
print list
list.delete()
# list.arr[0],list.arr[-1] = list.arr[-1],list.arr[0]
# list.arr.pop()
# list.prelocate(0,len(list.arr))

print list
