'''
Search a target value inside Matrix whose rows are sorted and elements are in increasing order throughout the matrix
'''

def myfun(matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if ((target >= matrix[i][0]) and (target <= matrix[i][n-1])):
                #BinarySearch
                low = 0
                high = n - 1
                mid = 0
                while (low <= high):
                    mid = (high + low) // 2
                    if(matrix[i][mid] == target):
                        return True
                    elif (matrix[i][mid] < target):
                        low = mid + 1
                    elif(matrix[i][mid] > target):
                        high = mid - 1
                else:
                    return False
            
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
ans = myfun(matrix, target)
print(ans)