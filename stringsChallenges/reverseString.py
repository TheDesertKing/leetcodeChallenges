def reverseString(s):
    left = 0
    right = len(s)-1
    while not left >= right:
        temp = s[right]
        s[right] = s[left]
        s[left] = temp
        left += 1
        right -= 1
        



def main():
    test = ['a','b','c','d','e','f','s']
    reverseString(test)
    print(test)
    
if __name__ == "__main__":
    main()
