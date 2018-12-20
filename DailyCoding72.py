import collections

v  = ["A","B","A","C","A","A"]
e = [(0, 1),
 (0, 2),
 (2, 3),
 (3, 4),
     (4)
     ]

v1 = ["A","B","C","A","C","B","B"]
e1 = [
    (0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(3,1)
]

def dfs(V,v,edges,track,ans,visited):
    # print track,v,visited,edges
    if v not in edges.keys() or len(edges[v]) == 0:
        arr =  [V[i] for i in track]
        hm = collections.Counter(arr)
        ans = max(ans,max(hm.values()))
        return ans

    for d in edges[v]:
        if d in visited:
            return float('inf')
        ans = max(ans,dfs(V,d,edges,track+[d],ans,visited+[d]))
    return ans



def solution(v,e):
    edges = collections.defaultdict(set)
    for edge in e:
        edges[edge[0]].add(edge[1])
        if edge[0] == edge[1]:
            return None
    print edges
    ans = 0
    for node in range(len(v)):
        # print node
        ans = dfs(v,node,edges,[node],ans,[node])
    return ans if ans < float('inf') else None

print  solution(v1,e1)