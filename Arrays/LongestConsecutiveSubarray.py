'''
Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.


Example 1:

Input:
N = 7
a[] = {2,6,1,9,4,5,3}
Output:
6
Explanation:
The consecutive numbers here
are 1, 2, 3, 4, 5, 6. These 6
numbers form the longest consecutive
subsquence.
Example 2:

Input:
N = 7
a[] = {1,9,3,10,4,20,2}
Output:
4
Explanation:
1, 2, 3, 4 is the longest
consecutive subsequence.

Your Task:
You don't need to read input or print anything. Your task is to complete the function findLongestConseqSubseq() which takes the array arr[] and the size of the array as inputs and returns the length of the longest subsequence of consecutive integers.


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).


Constraints:
1 <= N <= 105
0 <= a[i] <= 105
'''

# Solution with O(n) time complexity and O(1) space complexity

def findLongestConseqSubseq(arr, N):
    # code here
    s = set()
    for i in range(N):
        s.add(arr[i])

    ans = 0
    for i in range(N):
        if ((arr[i] - 1) not in s):
            j = arr[i] + 1
            while(j in s):
                j += 1

            ans = max(ans, j - arr[i])

    return ans

if __name__ == '__main__':
    ar = list(map(int, input("Enter num of arr >> ").split()))
    n = len(ar)
    answer = findLongestConseqSubseq(ar, n)
    print(answer)