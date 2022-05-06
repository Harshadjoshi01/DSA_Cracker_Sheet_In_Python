'''
Find Factorial of Large Number
'''

def factorial(N):
    # code here
    res = 1

    for i in range(2, N+1):
        res *= i
    return res

if __name__ == "__main__":
    num = int(input("Enter num >> "))
    answer = factorial(num)
    print(answer)
