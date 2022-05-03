def MaxSumContinuousSubarray(arr):
    maxi = arr[0]
    summ = 0;
    ar_len = len(arr)
    for i in range(ar_len):
        summ += arr[i]
        if (summ > maxi):
            maxi = summ
        if (summ < 0):
            summ = 0
    return maxi

if __name__ == '__main__':
    arr = [8,5,4,6,-14,7,4,5]
    print(MaxSumContinuousSubarray(arr))
