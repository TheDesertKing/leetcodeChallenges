"""This solution contains an optimization regarding leading zeroes, so it will only loop through numbers until the leading zeroes"""


def moveZeroes(nums) -> None:
    iterator = 0
    shift = 0
    end = 0
    for i in range(len(nums)-1,0,-1):
        if nums[i] != 0:
            end = i
            break

    while iterator <= end:
        if nums[iterator] == 0:
            shift += 1 
        elif shift > 0:
            nums[iterator-shift] = nums[iterator]
            nums[iterator] = 0
        iterator += 1






def main():
    tests = {1: [1,2,3,0,5,0,7,0,0,2,3,0],
             2:[1,2,0,0,0],
             3:[0,0,1,2,3,0,4],
             4:[0,0,0,0],
             5:[0,1,0]}

    for key in tests.keys():
        moveZeroes(tests[key])
        print(tests[key])

if __name__ == "__main__":
    main()

