import random as r
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        ret = ''
        temp = self
        while temp.next:
            ret += str(temp.val)+'->'
            temp = temp.next
        ret += str(temp.val)
        return ret

def initTest(vals=None,random=False,sortedRandom=False):
    if vals:
        test =  ListNode(vals[0])
        test.next = ListNode(vals[1])
        test.next.next = ListNode(vals[2])
        test.next.next.next = ListNode(vals[3])
    elif random:
        test =  ListNode(r.randint(0,9))
        test.next = ListNode(r.randint(0,9))
        test.next.next = ListNode(r.randint(0,9))
        test.next.next.next = ListNode(r.randint(0,9))
    elif sortedRandom:
        values = sorted([r.randint(0,9) for i in range(4)])
        test =  ListNode(values[0])
        test.next = ListNode(values[1])
        test.next.next = ListNode(values[2])
        test.next.next.next = ListNode(values[3])
    else:
        test =  ListNode(2)
        test.next = ListNode(3)
        test.next.next = ListNode(4)
        test.next.next.next = ListNode(5)
    print(test)
    return test
