class LinkNode:
    def __init__(self,val):
        self.val = val
        self.next = None


head = LinkNode(1)
cur = head

for i in range(2,10):
    cur.next = LinkNode(i)
    cur = cur.next


def printList(head):
    cur = head
    while cur:
        print cur.val,
        cur = cur.next
    print


def solution(head):
    p = head.next
    ch = head

    while head.next:
        head.next = p.next
        p.next = ch
        ch = p
        p = head.next
    return ch


printList(solution(head))
