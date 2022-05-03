def movenegativeToOneSideArray(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] < 0:
            if arr[right] >= 0:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            else:
                right -= 1
        else:
            left += 1
    return arr

if __name__ == '__main__':
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    print(movenegativeToOneSideArray(arr))
    