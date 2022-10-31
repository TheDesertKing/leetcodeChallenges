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
    

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

def main():
    test =  ListNode(2)
    test.next = ListNode(3)
    test.next.next = ListNode(4)
    test.next.next.next = ListNode(5)
    print(test)
    if test:
        deleteNode(test)
    tests = []
    if tests:
        for test in tests:
            print(test,'->',function(test))
    
if __name__ == "__main__":
    main()
