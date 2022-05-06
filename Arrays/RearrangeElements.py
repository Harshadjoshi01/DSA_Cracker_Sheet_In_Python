'''
Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is followed by negative and vice-versa maintaining the order of appearance. 
Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.

Examples : 

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}

'''
#Approch: firstly seprating positive and negative elements inplace without using extra space and than rearranging them

def RearrangeElements(arr, n):
    i = 0
    j = n -1
    while (i < j):
        while(arr[i] >= 0 and i <= n -1):
            i += 1
        while(arr[j] < 0 and j <= n -1):
            j -= 1
        if(i < j):
            arr[i], arr[j] = arr[j], arr[i]
        
    
    if(i == 0 or i == n):
        return
    
    k = 0
    while(i < n and i < n):
        arr[k], arr[i] = arr[i], arr[k]
        i += 1
        k += 2

    return arr

if __name__ == '__main__':
    arr = list(map(int, input("Enter num of arr >> ").split()))
    n = len(arr)
    answer = RearrangeElements(arr, n)
    print(answer)