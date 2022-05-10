'''
Given a matrix of size r*c. Traverse the matrix in spiral form.

Example 1:

Input:
r = 4, c = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15,16}}
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
Explanation:

Example 2:

Input:
r = 3, c = 4  
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12}}
Output: 
1 2 3 4 8 12 11 10 9 5 6 7
Explanation:
Applying same technique as shown above, 
output for the 2nd testcase will be 
1 2 3 4 8 12 11 10 9 5 6 7.

Your Task:
You dont need to read input or print anything. Complete the function spirallyTraverse() that takes matrix, r and c as input parameters and returns a list of integers denoting the spiral traversal of matrix. 

Expected Time Complexity: O(r*c)
Expected Auxiliary Space: O(r*c), for returning the answer only.

Constraints:
1 <= r, c <= 100
0 <= matrixi <= 100
'''
def spirallyTraverse(matrix, r, c): 
        # code here 
        top = 0 
        bottom = r - 1
        left = 0
        right = c - 1
        final = []
        while (True):
            
            if left > right:
                break
            
            for i in range(left,right+1):
                final.append(matrix[top][i])
            top += 1
            
            if top > bottom:
                break
            
            for i in range(top,bottom+1):
                final.append(matrix[i][right])
            right -= 1
            
            if left > right:
                break
            
            for i in range(right, left - 1, -1):
                final.append(matrix[bottom][i])
            bottom -= 1
            
            if top > bottom:
                break
            
            for i in range(bottom, top - 1, -1):
                final.append(matrix[i][left])
            left += 1
        
        return final
            
        

l = [[6, 6, 2, 28, 2], [12, 26, 3, 28, 7], [22, 25, 3, 4, 23]]
r = 3
c = 5
ans = spirallyTraverse(l, r, c)
print(ans)
