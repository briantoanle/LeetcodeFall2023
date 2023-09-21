
'''


i = i or i = i + j
j = j + 1
                            i = 0 j = 1
                           /           \
                    i=0 j = 2               i=1 j = 2
                    /       \               /      \
                i=0 j=3    i=2 j=3       i=1 j=3   i=3 j=3
                /     \       /     \      /   \
      i=0 j=4  i=3 j=4   i=2 j=4 i=5 j=4  i=1 j=4  i=4 j=4    i=3 j=4

i=0 j=5  i=4 j=5  i=3 j=5  i=7 j=5  i=2 j=5 i=6 j=5  i=5 j=5 i=9 j=5 i=1 j=5 i=5 j=5  i=4 j=5 i=8 j=5  i=3 j=5 i=7 j=5


                                                        [0, 1]
                                    /                                         \
                                [0,2]                                              [1, 2]
                        /                   \                             /                   \
                  [0,3]                   [2,3]                       [1,3]                       [3,3]
            /           \                /           \               /           \               /           \
       [0,4]          [3,4]          [2,4]          [5,4]         [1,4]          [4,4]        [3,4]          [6,4] XXXX
   /        \      /        \       /   \       /       \      /      \         /    \      /      \
[0,5]    [4,5]   [3,5]   [7,5] [2,5]  [6,5]  [5,5]    [9,5] [1,5]   [5,5]   [4,5] [8,5]  [3,5]   [7,5]

F(n) = max(  F(step + 1, i,j+1), F(step+1, i+j, j+1)
'''


def maxIndex2(steps,badIndex,step=0,i = 0,j = 1):
    #print(i,j,sum)
    if j >= steps:
        return 0
    if i != badIndex:
        return max(maxIndex2(steps, badIndex, step + 1, i,j+1), maxIndex2(steps,badIndex,step+1, i+j, j+1))
    return 0


def maxIndex(steps: int, badIndex: int) -> int:

    def recursion(i: int, j: int,dict={}) -> int:
        tempStr = str(j) + str(i)
        if tempStr in dict:
            return dict[tempStr]
        if j == steps + 1:
            return i
        if i == badIndex:
            return 0
        else:
            if tempStr not in dict:
                dict[tempStr] = max(recursion(i, j+1), recursion(i+j, j+1))
            return dict[tempStr]

    return recursion(0, 1)


print(maxIndex(4,6)) # -> should return 9
print(maxIndex(2,2)) # -> should return 3
print(maxIndex(3,3)) # -> should return 9
# one more test case I know, input: 40, 10, this should return 819
print(maxIndex(40,10))