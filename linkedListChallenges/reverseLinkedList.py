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

def reverseList(head):
    if not head:
        return None
    ret = ListNode(head.val)
    while head.next:
        newHead = ListNode(head.next.val)
        newHead.next = ret
        ret = newHead
        head = head.next
    return ret


def main():
    test =  ListNode(2)
    test.next = ListNode(3)
    test.next.next = ListNode(4)
    test.next.next.next = ListNode(5)
    if test:
        print(reverseList(test))
    tests = []
    if tests:
        for test in tests:
            print(test,'->',function(test))
    
if __name__ == "__main__":
    main()
