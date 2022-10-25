
def isAnagram(s,t):
    if set(s) != set(t) or len(s) != len(t):
        return False
    if list(sorted(s)) != list(sorted(t)):
        return False
    return True

def main():
    test = ['anagram','aangran']
    print(isAnagram(*test))
    
if __name__ == "__main__":
    main()
