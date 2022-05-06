'''
Given three arrays sorted in non-decreasing order, print all common elements in these arrays.

'''

# Solution 1 using sets in python


def commonElements(A, B, C, n1, n2, n3):
    # your code here
    A = set(A)
    B = set(B)
    C = set(C)
    final = list(C.intersection(A, B))
    final.sort()
    return final

# Solution 2 without using any other data structure 

# Python function to print common elements in three sorted arrays
def findCommon(ar1, ar2, ar3, n1, n2, n3):

    # Initialize starting indexes for ar1[], ar2[] and ar3[]
    i, j, k = 0, 0, 0

    # Iterate through three arrays while all arrays have elements
    while (i < n1 and j < n2 and k < n3):

        # If x = y and y = z, print any of them and move ahead
        # in all arrays
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
            print(ar1[i])
            i += 1
            j += 1
            k += 1 

        # x < y
        elif ar1[i] < ar2[j]:
            i += 1

        # y < z
        elif ar2[j] < ar3[k]:
            j += 1

        # We reach here when x > y and z < y, i.e., z is smallest
        else:
            k += 1

if __name__ == '__main__':
    ar1 = list(map(int, input("Enter elements of first arr >> ").split()))
    ar2 = list(map(int, input("Enter elements of Second arr >> ").split()))
    ar3 = list(map(int, input("Enter elements of third arr >> ").split()))
    n1 = len(ar1)
    n2 = len(ar2)
    n3 = len(ar3)
    answer = commonElements(ar1, ar2, ar3, n1, n2, n3)
    print(answer)
