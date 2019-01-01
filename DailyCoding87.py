import collections
input = [
    "A N B",
    "B NE C",
    "C N A"
]

input2 = [
    "A NW B",
    "A N B"
]


input3 = [
    "A N B",
    "B N C",
    "C NE E",
    "C W D",
    "D E E"
]
class node:
    def __init__(self,val):
        self.val = val
        self.N = []
        self.S = []
        self.W = []
        self.E = []

    def getarr(self,d):
        if d == "N":
            return self.N
        if d == "W":
            return self.W
        if d == "E":
            return self.E
        if d == "S":
            return self.S

def solution(rules):
    hm = {}
    rev = {
        "N":"S",
        "S":"N",
        "E":"W",
        "W":"E"
    }

    for rule in rules:
        left, ds, right = rule.split(" ")
        if left not in hm or right not in hm:
            hm[left] = hm.get(left, node(left))
            hm[right] = hm.get(right, node(right))

            for d in ds:
                print left +" at "+ " "+ d + " of "+ right
                print right +" at "+ " "+ rev[d] + " of "+ left

                hm[right].getarr(d).append(left)
                hm[left].getarr(rev[d]).append(right)

                for d2 in ["N", "W", "S", "E"]:
                    if d2 == d:
                        continue
                    for n in hm[right].getarr(d2):
                        hm[n].getarr(d).append(left)

                for d2 in ["N", "W", "S", "E"]:
                    if d2 == rev[d]:
                        continue
                for n in hm[left].getarr(d2):
                    hm[n].getarr(rev[d]).append(right)


        else:
            #validate:
            for d in ds:
                if left not in hm[right].getarr(d):
                    for key in hm:
                        print
                        print key
                        print
                        for d in ["N", "W", "S", "E"]:
                            print d.lower(), hm[key].getarr(d)
                    return False
                elif right not in hm[left].getarr(rev[d]):
                    for key in hm:
                        print
                        print key
                        print
                        for d in ["N", "W", "S", "E"]:
                            print d.lower(), hm[key].getarr(d)
                    return False


    return True



print solution(input3)