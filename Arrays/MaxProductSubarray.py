'''
Given an array Arr[] that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.

Example 1:

Input:
N = 5
Arr[] = {6, -3, -10, 0, 2}
Output: 180
Explanation: Subarray with maximum product
is [6, -3, -10] which gives product as 180.
Example 2:

Input:
N = 6
Arr[] = {2, 3, 4, 5, -1, 0}
Output: 120
Explanation: Subarray with maximum product
is [2, 3, 4, 5] which gives product as 120.
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxProduct() which takes the array of integers arr and n as parameters and returns an integer denoting the answer.
Note: Use 64-bit integer data type to avoid overflow.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 500
-102 ≤ Arri ≤ 102
'''
import math

#Solution O(n) Time Complexity and O(1) space complexity
def maxProduct(self, arr, n):
     # code here
    curr_product_1 = 1
    max_product_1 = -math.inf
    for i in range(n):
        curr_product_1 *= arr[i]
        max_product_1 = max(curr_product_1, max_product_1)
        if(arr[i] == 0):
            curr_product_1 = 1

    curr_product_2 = 1
    max_product_2 = -math.inf
    for i in range(n-1, -1, -1):
        curr_product_2 *= arr[i]
        max_product_2 = max(curr_product_2, max_product_2)
        if(arr[i] == 0):
            curr_product_2 = 1

    return max(max_product_1, max_product_2)

if __name__ == '__main__':
    ar = list(map(int, input("Enter arr elements >> ").split()))
    n = len(ar)
    answer = maxProduct(ar, n)
    print(answer)