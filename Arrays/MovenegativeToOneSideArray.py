'''
An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
Note: Order of elements is not important here.

'''

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
    