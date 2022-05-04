'''
Given an array of integers. Find the Inversion Count in the array.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum.
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.


Example 1:

Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5
has three inversions (2, 1), (4, 1), (4, 3).
Example 2:

Input: N = 5
arr[] = {2, 3, 4, 5, 6}
Output: 0
Explanation: As the sequence is already
sorted so there is no inversion count.
Example 3:

Input: N = 3, arr[] = {10, 10, 10}
Output: 0
Explanation: As all the elements of array
are same, so there is no inversion count.
Your Task:
You don't need to read input or print anything. Your task is to complete the function inversionCount() which takes the array arr[] and the size of the array as inputs and returns the inversion count of the given array.

Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 5*105
1 ≤ arr[i] ≤ 1018
'''

# Solution 1 O(n^2) Time Complexity

def inversionCount(arr, n):
       # Your Code Here
    if(arr == arr[:].sort()):
        return 0

    if arr == arr[::-1]:
        x = n - 1
        y = (x*(x + 1)) / 2
        return int(y)

    if (len(set(arr)) == 1):
        return 0

    count = 1
    inversion = 0
    for num in arr:
        for x in arr[count:]:
            if (num > x):
                inversion += 1
        count += 1

    return inversion


if __name__ == '__main__':
    ls = input("Enter num in list >> ").split()
    ls1 = []
    for i in range(len(ls)):
        ls1.append(int(ls[i]))
    answer = inversionCount(ls1, len(ls1))
    print(answer)