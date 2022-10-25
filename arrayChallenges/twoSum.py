def twoSum(nums, target):
    def findInSorted(nums,num):
        mid = len(nums)//2
        
        if nums[mid] == num:
            return True
        elif len(nums) == 1:
            return False
        elif nums[mid] > num:
            return findInSorted(nums[:mid],num)
        else:
            if len(nums) == 2:
                return False
            return findInSorted(nums[mid:],num)


    sort = sorted(nums)    
    i = 0
    while i < len(nums):
        num = nums[i]
        j = sort.index(num)
        if findInSorted(sort[:j] + sort[j+1:],target-num):
            return i,nums.index(target-nums[i],i+1)
        i += 1


def main():
    tests = [1,22,31,53,53]
    tests = [0,4,3,0]
    target= 0
    print(twoSum(tests,target))
    
if __name__ == "__main__":
    main()
