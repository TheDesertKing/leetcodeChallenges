def firstUniqChar(s):
    i = 0
    while i < len(s):
        if s.count(s[i]) == 1:
            return i
        i+=1
    return -1


def main():
    tests = ['abca','bbbaeaecd']
    for test in tests:
        print(test,'->',firstUniqChar(test))
    
if __name__ == "__main__":
    main()
