def myAtoi(s):
    if s == '': return 0
    i = 0
    while i < len(s):
        if s[i] != ' ':
            break
        i+= 1
    if i == len(s):
        return 0
    ret = '0'
    isNegative = False
    if s[i] == '-':
        isNegative = True
        i+=1 
    elif s[i] == '+':
        i+=1 

    for char in s[i:]:
        if not char.isnumeric():
            break
        else:
            ret += char

    if isNegative: ret = -int(ret)
    else: ret = int(ret)
    if ret > 2**31-1:
        return 2**31-1
    if ret < -2**31:
        return -2**31
    return ret

def main():
    test = 0
    if test:
        print(function(test))
    tests = ['1234','-1234','   52ABC',str(2**32)]
    if tests:
        for test in tests:
            print(test,'->',myAtoi(test))
    
if __name__ == "__main__":
    main()
