'''
Given an array arr of size n and an integer X. Find if there's a triplet in the array which sums up to the given integer X.


Example 1:

Input:
n = 6, X = 13
arr[] = [1 4 45 6 10 8]
Output:
1
Explanation:
The triplet {1, 4, 8} in 
the array sums up to 13.
Example 2:

Input:
n = 5, X = 10
arr[] = [1 2 4 3 6]
Output:
1
Explanation:
The triplet {1, 3, 6} in 
the array sums up to 10.

Your Task:
You don't need to read input or print anything. Your task is to complete the function find3Numbers() which takes the array arr[], the size of the array (n) and the sum (X) as inputs and returns True if there exists a triplet in the array arr[] which sums up to X and False otherwise.


Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ n ≤ 103
1 ≤ A[i] ≤ 105
'''

def find3Numbers(A, n, X):
        count = 0
        for i in range(0, n-1):
            # Find pair in subarray A[i + 1..n-1]
            # with sum equal to sum - A[i]
            s = set()
            curr_sum = X - A[i]
            for j in range(i + 1, n):
                if (curr_sum - A[j]) in s:
                    count += 1
                s.add(A[j])
     
        return count

if __name__ == '__main__':
    ar = list(map(int, input("Enter elements >> ").split()))
    n = len(ar)
    x = int(input("Enter sum >> "))
    answer = find3Numbers(ar, n, x)
    print(answer)