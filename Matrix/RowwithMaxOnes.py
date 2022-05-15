'''
Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.

Example 1:

Input:
N = 4 , M = 4
Arr[][] = {{0, 1, 1, 1},
           {0, 0, 1, 1},
           {1, 1, 1, 1},
           {0, 0, 0, 0}}
Output: 2
Explanation: Row 2 contains 4 1's (0-based
indexing).

Example 2:

Input:
N = 2, M = 2
Arr[][] = {{0, 0}, {1, 1}}
Output: 1
Explanation: Row 1 contains 2 1's (0-based
indexing).

Your Task:
You don't need to read input or print anything. Your task is to complete the function rowWithMax1s() which takes the array of booleans arr[][], n and m as input parameters and returns the 0-based index of the first row that has the most number of 1s. If no such row exists, return -1.


Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(1)
'''


def rowWithMax1s(self, arr, n, m):
    # code here
    max_num = 0
    max_idx = 0
    for i in range(n):
        if sum(arr[i]) > max_num:
            max_num = sum(arr[i])
            max_idx = i

    if (max_num > 0):
        return max_idx
    else:
        return -1

if __name__ == '__main__':
    r, c = map(int, input("Enter row and column >> ").strip().split())
    zeromatrix = [[0 for j in range(c)] for i in range(r)]
    matrix = [int(x) for x in input("Enter nums in matrix >> ").strip().split()]
    k = 0
    for i in range(r):
        for j in range(c):
            zeromatrix[i][j] = matrix[k]
            k += 1
    
    ans = rowWithMax1s(zeromatrix, r, c)
    print(ans)