from linkedListClassAndTests import *

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
    test = initTest()
    if test:
        print(reverseList(test))
    tests = []
    if tests:
        for test in tests:
            print(test,'->',function(test))
    
if __name__ == "__main__":
    main()
