'''
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.


Example 1:

Input:
N = 4, K = 6
arr[] = {1, 5, 7, 1}
Output: 2
Explanation:
arr[0] + arr[1] = 1 + 5 = 6
and arr[1] + arr[3] = 5 + 1 = 6.

Example 2:

Input:
N = 4, K = 2
arr[] = {1, 1, 1, 1}
Output: 6
Explanation:
Each 1 will produce sum 2 with any 1.

Your Task:
You don't need to read input or print anything. Your task is to complete the function getPairsCount() which takes arr[], n and k as input parameters and returns the number of pairs that have sum K.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 105
1 <= K <= 108
1 <= Arr[i] <= 106
'''


def getPairsCount(arr, n, k):
     # code here
    unordered_map = {}
    count = 0
    for i in range(n):
        if (k - arr[i]) in unordered_map:
            count += unordered_map[k - arr[i]]
        if arr[i] in unordered_map:
            unordered_map[arr[i]] += 1
        else:
            unordered_map[arr[i]] = 1
    return count

if __name__ == '__main__':
    ls = list(map(int, input("Enter the numbers >> ").split()))
    k = int(input("Enter sum value >> "))
    n = len(ls)
    answer = getPairsCount(ls, n, k)
    print(answer)