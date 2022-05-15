'''
Given a row wise sorted matrix of size RxC where R and C are always odd, find the median of the matrix.

Example 1:

Input:
R = 3, C = 3
M = [[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]]

Output: 5

Explanation:
Sorting matrix elements gives us 
{1,2,3,3,5,6,6,9,9}. Hence, 5 is median. 
 

Example 2:

Input:
R = 3, C = 1
M = [[1], [2], [3]]
Output: 2

Your Task:  
You don't need to read input or print anything. Your task is to complete the function median() which takes the integers R and C along with the 2D matrix as input parameters and returns the median of the matrix.

Expected Time Complexity: O(32 * R * log(C))
Expected Auxiliary Space: O(1)


Constraints:
1<= R,C <=150
1<= matrix[i][j] <=2000
'''

from bisect import bisect_right as upper_bound
MAX = 100;
def median(self, m, r, d):
    	#code here 
        mi = m[0][0]
        mx = 0
        for i in range(r):
            if m[i][0] < mi:
                mi = m[i][0]
            if m[i][d-1] > mx :
                mx =  m[i][d-1]
     
        desired = (r * d + 1) // 2
     
        while (mi < mx):
            mid = mi + (mx - mi) // 2
            place = [0];
         
            # Find count of elements smaller than mid
            for i in range(r):
                j = upper_bound(m[i], mid)
                place[0] = place[0] + j
            if place[0] < desired:
                mi = mid + 1
            else:
                mx = mid
    
        return mi

if __name__ == '__main__':
    r, c = map(int, input("Enter row and column >> ").strip().split())
    zeromatrix = [[0 for j in range(c)] for i in range(r)]
    matrix = [int(x) for x in input("Enter nums in matrix >> ").strip().split()]
    k = 0
    for i in range(r):
        for j in range(c):
            zeromatrix[i][j] = matrix[k]
            k += 1
    
    ans = median(zeromatrix, r, c)
    print(ans)