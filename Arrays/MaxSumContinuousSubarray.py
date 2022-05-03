'''
Kadane's Algorithm 
Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.


Example 1:

Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
Example 2:

Input:
N = 4
Arr[] = {-1,-2,-3,-4}
Output:
-1
Explanation:
Max subarray sum is -1 
of element (-1)

Your Task:
You don't need to read input or print anything. The task is to complete the function maxSubarraySum() which takes Arr[] and N as input parameters and returns the sum of subarray with maximum sum.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 106
-107 ≤ A[i] ≤ 107
'''

def MaxSumContinuousSubarray(arr):
    maxi = arr[0]
    summ = 0;
    ar_len = len(arr)
    for i in range(ar_len):
        summ += arr[i]
        if (summ > maxi):
            maxi = summ
        if (summ < 0):
            summ = 0
    return maxi

if __name__ == '__main__':
    arr = [8,5,4,6,-14,7,4,5]
    print(MaxSumContinuousSubarray(arr))
