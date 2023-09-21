
def testCase1():
    s = 'abcdef'
    print(reverse(s))   # eventually, this should print: fedcba

def reverse2(s):
    mid = len(s) // 2

    left = 1
    s = s[-1] + s[1:-1] + s[0]
    print(s)
    while left < mid:
        print(left,s[-left-1],s[left])
        print("this line," +  s[-left-1] + s[left:-left] + s[left])
        s = s[-left-1] + s[left:-left] + s[left]
        left+=1
    print(s)

def reverse3(q):
    '''temp = ''
    for i in range(len(q)-1,-1,-1):
        temp+=q[i]
    print(temp)'''
    return q[::-1]

def reverse(q):

    if q == '':
        return ""
    #print("char here", q[0])
    c = q[0]
    return reverse(q[1:]) + c
    # print("char there", c)


# check if the string isPalindrome
# return True if it is
# "racecar" --> True
# "hello" --> False
def recursion1():
    print(recursion('racecar'))


def recursion(s):
    print(s)
    if s[0] != s[len(s)-1]:
        return False

    if s == "" or len(s) == 1:
        return True

    return recursion(s[1:(len(s)-1)])

recursion1()
#testCase1()
