def UnionIntersectionOfSortedArray(arr1, arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    print("Intersection of Arrays: ", result)

    for num in arr1 + arr2:
        if num not in result:
            result.append(num)
    
    print("Union of Arrays: ", result)



if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(UnionIntersectionOfSortedArray(arr1, arr2))