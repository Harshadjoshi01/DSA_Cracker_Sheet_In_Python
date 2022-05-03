def minmaxinarray(arr):
    min = arr[0]
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    
    return min, max

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(minmaxinarray(arr))