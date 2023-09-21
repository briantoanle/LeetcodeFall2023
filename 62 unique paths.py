

# **** com

# beginning coordinates = 1,1
# m is height
# n is width

# uniquePaths(3,7) # output should be 28

"""
[x]         -> m = 1, n = 1: how many possibility: 1
[x x]       -> m = 1, n = 2: how many possibility: 1
[x
 x]         -> m = 2, n = 1: how many possibility: 1

[x x 
 x x]       -> m = 2, n = 2: how many possibility: 2
 
 [x x x     -> m = 2, m = 3: possibilities: 3
  x x x]

 [x x
  x x        -> m = 3, n = 2: possibilities: 3
  x x]

  [x x x
   x x x     -> m = 3, n = 3:
   x x x]
                                          =6
                                         (3,3)
                            /=3                       \=3
                       (2,3)                            (3,2)
                    /=1           \=2               /=1         \=2
                (1,3)           (2,2)               (3,1)        (2,2)
            /=0      \=1       /=1   \=1         /=1    \=0     /=1  \=1
          (0,3)     (1,2)    (1,2)  (2,1)         (2,1)  (3,0)  (1,2) (2,1)
                    /=0        /      \             /             /        \
                (0,1) (1,1)  (0,2)(1,1)\          (1,1) (2,0)    (0,2)(1,1) \
                                       (1,1)(2,0)                           (1,1)(2,0)


        the recursion: return f(m-1, n) + f(m, n-1)

        base case 1: m = 1 and n = 1
        base case 2: either m = 0 or n = 0


"""
from datetime import *

def UP(m,n):
    print('here')




UP(3,2)

def sixtwopaths(m,n):
    memo = {}

    return uniquePathsRecursion(m,n,memo)

def uniquePathsRecursion(m, n,memo):
    key = str(m) + ' ' + str(n)
    if key in memo:
        return memo[key]
    if m == 1 or n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    value = uniquePathsRecursion(m - 1, n,memo) + uniquePathsRecursion(m, n - 1,memo)

    memo[key] = value
    print(memo)
    return memo[key]

start = datetime.now()
print(start)
print(sixtwopaths(3,3))
end = datetime.now()
print(end)
print("Execution time =", end - start)
