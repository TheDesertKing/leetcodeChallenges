from linkedListClassAndTests import *

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

def main():
    test = initTest()
    if test:
        deleteNode(test)
    tests = []
    if tests:
        for test in tests:
            print(test,'->',function(test))
    
if __name__ == "__main__":
    main()
