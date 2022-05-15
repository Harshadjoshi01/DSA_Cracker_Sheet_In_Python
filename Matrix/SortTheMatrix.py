'''
Given an NxN matrix Mat. Sort all elements of the matrix.

Example 1:

Input:
N=4
Mat=[[10,20,30,40],
[15,25,35,45]
[27,29,37,48]
[32,33,39,50]]
Output:
10 15 20 25
27 29 30 32
33 35 37 39
40 45 48 50
Explanation:
Sorting the matrix gives this result.
Example 2:

Input:
N=3
Mat=[[1,5,3],[2,8,7],[4,6,9]]
Output:
1 2 3
4 5 6
7 8 9
Explanation:
Sorting the matrix gives this result.
Your Task:
You don't need to read input or print anything. Your task is to complete the function sortedMatrix() which takes the integer N and the matrix Mat as input parameters and returns the sorted matrix.


Expected Time Complexity:O(N2LogN)
Expected Auxillary Space:O(N2)


Constraints:
1<=N<=1000
1<=Mat[i][j]<=105
'''

def sortedMatrix(self, N, M):
    # code here
    my_ls = []
    for i in range(N):
        for j in range(N):
            my_ls.append(M[i][j])

    my_ls.sort()
    k = 0
    for i in range(N):
        for j in range(N):
            M[i][j] = my_ls[k]
            k += 1

    return M

if __name__ == '__main__':
    r, c = map(int, input("Enter row and column >> ").strip().split())
    zeromatrix = [[0 for j in range(c)] for i in range(r)]
    matrix = [int(x) for x in input("Enter nums in matrix >> ").strip().split()]
    k = 0
    for i in range(r):
        for j in range(c):
            zeromatrix[i][j] = matrix[k]
            k += 1
    
    ans = sortedMatrix(zeromatrix, r, c)
    print(ans)