def longestCommonPrefix(strs):
    prefix = ''
    for char in min(strs,key=len):
        prefix += char
        if not all(s.startswith(prefix) for s in strs):
            return prefix[:-1]
    return prefix


def main():
    test = 0
    if test:
        print(function(test))
    tests = [['flower','flow','flucker'],['flower','flowe','flow'],['flower','flow','a','f'],['flower','flow','f']]
    if tests:
        for test in tests:
            print(test,'->',longestCommonPrefix(test))
    
if __name__ == "__main__":
    main()
