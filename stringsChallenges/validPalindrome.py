import re
def isPalindrome(s):
    if ''.join(list(reversed(re.sub(r'[^a-z]','',s.lower())))) == re.sub(r'[^a-z]','',s.lower()):
        return True
    return False
    

def main():
    test = "A man, a plan, a canal: Panama"
    if test:
        print(isPalindrome(test))
    tests = []
    if tests:
        for test in test:
            print(test,'->',function(test))
    
if __name__ == "__main__":
    main()
