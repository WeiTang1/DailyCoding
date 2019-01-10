input = ["A N B","B NE C","C N A"]
input2 = ["A NW B", "A N B"]
input3 = [
    "A N B",
    "B N C",
    "C NE E",
    "C W D",
    "D E E"
]
input4 = ["A N B", "B N C"]
#
#  A
#  B
#  CD
# E
class node:
    def __init__(self,val):
        self.val = val
        self.N = set()
        self.S = set()
        self.W = set()
        self.E = set()

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
    def putin(origin, target , d):
        hm[origin].getarr(d).add(target)
        hm[target].getarr(rev[d]).add(origin)
    for rule in rules:
        origin, ds, target = rule.split(" ")
        if origin not in hm or target not in hm:
            hm[origin] = hm.get(origin, node(origin))
            hm[target] = hm.get(target, node(target))
            for d in ds:
                putin(origin,target,d)
        else:
            for key in hm:
                print
                print key
                print
                for d in ["N", "W", "S", "E"]:
                    print d.lower(), hm[key].getarr(d)

    return True



print solution(input3)