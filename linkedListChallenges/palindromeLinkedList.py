from linkedListClassAndTests import *
from reverseLinkedList import reverseList

def isPallendrome(head):
    i,j = head,head
    while j:
        i = i.next
        j = j.next.next
    r = reverseList(i)
    while r and r.val == head.val:
        r = r.next
        head = head.next
    if r:
        return False
    return True

def main():
    test = initTest(vals=[4,3,3,4])
    if test:
        print(isPallendrome(test))
    tests = []
    if tests:
        for test in tests:
            print(test,'->',function(test))
    
if __name__ == "__main__":
    main()
