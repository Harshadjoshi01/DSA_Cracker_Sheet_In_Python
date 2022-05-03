def find_duplicate(nums):
        for num in nums:
            if (nums[abs(num)] <= 0):
                return abs(num)
                break
            nums[abs(num)] = -nums[abs(num)]
    
if __name__ == '__main__':
    ar = [1,3,4,2,2]            #nums in arr are in range (1 to n)
    print(find_duplicate(ar))