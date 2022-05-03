def rotate_an_array_by_one(arr):
    index = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = index
    return arr

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(rotate_an_array_by_one(arr))
