from linkedListClassAndTests import *

#trying to do this in-place into list1
def mergeTwoLists(list1,list2):
    if not list1:
        return list2
    if not list2:
        return list1
    head = list1
    #to track the node inserted before list1's first node
    #to connect more nodes before list1's first node
    lastInserted = None

    while list2 and list1.val > list2.val:
        #insert node to the start of list make head point to it
        temp = ListNode(list2.val)
        temp.next = list1
        if lastInserted:
            lastInserted.next = temp
        else:
            head = temp
        lastInserted = temp
        list2 = list2.next

    while list2:
        if not list1.next:
            list1.next = list2
            return head
        if list1.next.val > list2.val:
            temp = ListNode(list2.val)
            temp.next = list1.next
            list1.next = temp
            list1 = list1.next
            list2 = list2.next
        else:
            list1 = list1.next

    return head






def main():
    test1 = initTest(sortedRandom=True)
    test1 = ListNode(5)
    test2 = initTest(sortedRandom=True)
    test2 = ListNode(1)
    test2.next = ListNode(2)
    test2.next.next = ListNode(4)
    print('\n')
    print(mergeTwoLists(test1,test2))
    tests = []
    if tests:
        for test in tests:
            print(test,'->',function(test))
    
if __name__ == "__main__":
    main()
