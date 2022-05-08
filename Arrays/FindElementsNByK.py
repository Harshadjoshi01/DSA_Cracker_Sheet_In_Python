'''
Given an array of size n, find all elements in array that appear more than n/k times. For example, if the input arrays 
is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output should be [2, 3]. Note that size of array is 8 (or n = 8), so 
we need to find all e
'''
from collections import Counter
def FindElements(ar, n, k):
    count = n // k
    Counter_dict = Counter(ar)

    for item in Counter_dict: # we can traverse inside a dict where items are keys and dict[item] are values
        if Counter_dict[item] > count:
            print(item, end=" ")

if __name__ == '__main__':
    ar = list(map(int, input("Enter the numbers >> ").split()))
    n = len(ar)
    k = int(input("Enter K >> "))
    FindElements(ar, n, k)

