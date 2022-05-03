def MinMaxDiffOfHights(arr, n, k):
    arr.sort()
    minEle = 0
    maxEle = 0
    result = arr[n-1] - arr[0]
    for i in range(1, n):
        if(arr[i] >= k):
            maxEle = max(arr[i-1]+k, arr[n-1]-k)
            minEle = min(arr[0]+k, arr[i]-k)
            result = min(result, maxEle-minEle)
    return result   

if __name__ == '__main__':
    arr = [1,10,14,14,14,15]
    n = 6
    k = 6
    print(MinMaxDiffOfHights(arr,n,k))
