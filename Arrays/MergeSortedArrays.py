def MergeSortedArrays(arr1, arr2):
    while (bool(arr1) or bool(arr2)):
        if(not bool(arr1)):
            for i in range(len(arr2)):
                print(arr2[i])
            arr2 = []
        elif(not bool(arr2)):
            for i in range(len(arr1)):
                print(arr1[i])
            arr1 = []
        elif(arr1[0] <= arr2[0]):
            print(arr1[0])
            arr1.pop(0)
        else:
            print(arr2[0])
            arr2.pop(0)

MergeSortedArrays([0,1,2,3],[5,6,7,8,9])