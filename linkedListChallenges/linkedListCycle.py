from linkedListClassAndTests import *

def hasCycle(head):
    if not head:
        return False
    s,f = head, head.next
    while f and f.next:
        if f == s:
            return True
        s = s.next
        f = f.next.next
    return False


def main():
    test = initTest()
    test.next.next.next.next = test
    if test:
        print(hasCycle(test))
    tests = []
    if tests:
        for test in tests:
            print(test,'->',function(test))

if __name__ == "__main__":
    main()
