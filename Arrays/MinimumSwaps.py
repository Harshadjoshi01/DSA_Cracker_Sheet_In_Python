'''
Given an array arr of n positive integers and a number k. One can apply a swap operation on the array any number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find the minimum number of swaps required to bring all the numbers less than or equal to k together, i.e. make them a contiguous subarray.

Example 1:

Input : 
arr[ ] = {2, 1, 5, 6, 3} 
K = 3
Output : 
1
Explanation:
To bring elements 2, 1, 3 together,
swap index 2 with 4 (0-based indexing),
i.e. element arr[2] = 5 with arr[4] = 3
such that final array will be- 
arr[] = {2, 1, 3, 6, 5}

Example 2:

Input : 
arr[ ] = {2, 7, 9, 5, 8, 7, 4} 
K = 6 
Output :  
2 
Explanation: 
To bring elements 2, 5, 4 together, 
swap index 0 with 2 (0-based indexing)
and index 4 with 6 (0-based indexing)
such that final array will be- 
arr[] = {9, 7, 2, 5, 4, 7, 8}
 

Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function minSwap() that takes an array (arr), sizeOfArray (n), an integer K, and return the minimum swaps required. The driver code takes care of the printing.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).


Constraints:
1 ≤ N ≤ 105
1 ≤ Arri, K ≤107
'''

def minSwap (arr, n, k) : 
    #Complete the function
    count = 0
    for i in range(n):
        if (arr[i] <= k):
            count += 1
    bad = 0
    for i in range(count):
        if (arr[i] > k):
            bad += 1
    front = 0
    back = count
    ans = bad
    while(back < n):
        if (arr[back] > k):
            bad += 1
        
        if (arr[front] > k):
            bad -= 1
        
        ans = min(ans, bad)
        front += 1
        back += 1
        
    return ans

if __name__ == '__main__':
    ar = list(map(int, input("Enter elements >> ").split()))
    n = len(ar)
    k = int(input("Enter k >> "))
    answer = minSwap(ar, n, k)
    print(answer)