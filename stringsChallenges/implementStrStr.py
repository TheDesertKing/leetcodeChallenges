def strStr(haystack, needle):
    j = 0
    i = 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            j+= 1
        else:
            i -= j
            j = 0
        if j == len(needle):
            return i-j+1
        i+=1
    return -1


def main():
    test = 0
    if test:
        print(function(test))
    tests = [['abcdef','abc'],['abcedf','edf'],['abcdef','nope']]
    if tests:
        for test in tests:
            print(test,'->',strStr(*test))
    
if __name__ == "__main__":
    main()
