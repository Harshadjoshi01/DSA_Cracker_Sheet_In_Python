def KthMaxMinArray(array, k):
    return sorted(array)[k-1]

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 5
    print(KthMaxMinArray(array, k))