def reverse(x):
    if x < 0: ret = 0-int(str(x)[:0:-1])
    else: ret = int(str(x)[::-1]) 
    if ret > 2**31-1 or ret < -2**31: return 0
    return ret
    


def main():
    tests = [12345,-12345,1000000009,1000000000]
    for test in tests:
        print(test,'->',reverse(test))
    print(1)
    
if __name__ == "__main__":
    main()
