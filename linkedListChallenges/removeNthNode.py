from linkedListClassAndTests import *

def removeNthFromEnd(head,n):
    nodeToRemove = head
    endFinder = head
    #move endFinder n nodes forward
    for i in range(n):
        #in case of n == len(linkedlist), no need to iterate,
        #just remove first node.
        if not endFinder.next:
            head = head.next
            return head
        endFinder = endFinder.next
    while endFinder.next:
        endFinder = endFinder.next
        nodeToRemove = nodeToRemove.next
    if n > 1:
        #move refrences to skip the removed node
        nodeToRemove.next.val = nodeToRemove.next.next.val
        nodeToRemove.next.next = nodeToRemove.next.next.next
    else:
        #remove refrences to last node, since n == 1
        nodeToRemove.next = None
        
    return head

def main():
    test = initTest()
    if test:
        print(removeNthFromEnd(test,1))
    tests = []
    if tests:
        for test in tests:
            print(test,'->',function(test))
    
if __name__ == "__main__":
    main()
