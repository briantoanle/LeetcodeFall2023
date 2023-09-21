'''
fibonacci dynamic programming

'''
from datetime import datetime

# time complexity is 2^n
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    # while n > 1:
    return fib(n-1) + fib(n-2)

# time complexity O(n)
def dpFib(n):
    # Fib(7)
    # 0 1 1 2 3 5 8 13
    arr = [0]*(n+1)
    arr[1] = 1
    for i in range(2,n+1):
        arr[i] = arr[i-1] +arr[i-2]

    return arr[n]


def dpFibMemo(n):
    memo = {}
    return dpFibMemoHelper(n, memo)


def dpFibMemoHelper(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = dpFibMemoHelper(n-1, memo) + dpFibMemoHelper(n-2, memo)
    memo[n] = result
    print("here", memo)
    return memo[n]



start = datetime.now()
print(start)
#for i in range(1, 8):
#    print(fib(i))
print(dpFibMemo(7))
# print(dpFib(7))
end = datetime.now()
print(end)
print("Execution time =", end-start)
