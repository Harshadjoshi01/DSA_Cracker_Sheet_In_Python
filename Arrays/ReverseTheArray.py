def reverseTheArray(arr):
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    return arr

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    print(reverseTheArray(arr))