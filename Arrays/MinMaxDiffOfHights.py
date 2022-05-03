'''
Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer. 
Find out the minimum possible difference of the height of shortest and longest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease by K to each tower.


Example 1:

Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output:
5
Explanation:
The array can be modified as 
{3, 3, 6, 8}. The difference between 
the largest and the smallest is 8-3 = 5.
Example 2:

Input:
K = 3, N = 5
Arr[] = {3, 9, 12, 16, 20}
Output:
11
Explanation:
The array can be modified as
{6, 12, 9, 13, 17}. The difference between 
the largest and the smallest is 17-6 = 11. 

Your Task:
You don't need to read input or print anything. Your task is to complete the function getMinDiff() which takes the arr[], n and k as input parameters and returns an integer denoting the minimum difference.


Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)

Constraints
1 ≤ K ≤ 104
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ 105
'''

def MinMaxDiffOfHights(arr, n, k):
    arr.sort()
    minEle = 0
    maxEle = 0
    result = arr[n-1] - arr[0]
    for i in range(1, n):
        if(arr[i] >= k):
            maxEle = max(arr[i-1]+k, arr[n-1]-k)
            minEle = min(arr[0]+k, arr[i]-k)
            result = min(result, maxEle-minEle)
    return result   

if __name__ == '__main__':
    arr = [1,10,14,14,14,15]
    n = 6
    k = 6
    print(MinMaxDiffOfHights(arr,n,k))
