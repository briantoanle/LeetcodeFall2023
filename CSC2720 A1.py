
# input: 2 sorted array
# output: array contains element in both


# ways:
# (1) O (m*n), loop join, loop through both arrays
# (2) O (nlog(m)) or vice versa, use binary search
# (3) O (m+n), linear solution, loop through both arrays, once each



# Big O of m * n
def find_duplicates1(arr1, arr2):

    # make new array to store the duplicates variable
    temp = []

    # loop through first array
    for i in arr1:
        # loop through second array
        for j in arr2:
            # if they're in both, add to temp array
            if i == j:
                # check for duplicates
                if i not in temp:
                    # store the duplicate in temp
                    temp.append(i)

    # return the result
    return temp

# big O of n * log m
# use binary search
def find_duplicates2(arr1,arr2):
    # make a temp array
    temp = []

    # make a binary search function
    def binary_search(arr, target):
        low = 0
        lengthArr = len(arr)
        high = lengthArr - 1
        result = None
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    # check which array is shorter to swap
    if len(arr1) > len(arr2):
        arr1,arr2 = arr2,arr1

    for i in arr1:
        found_in_arr2 = binary_search(arr2,i)
        if found_in_arr2 != -1:
            if i not in temp:
                temp.append(i)

    return temp
    # loop through arr1

def find_duplicates3(arr1,arr2):

    lengthArr1 = len(arr1)
    lengthArr2 = len(arr2)

    left, right = 0,0
    temp = []
    while left < lengthArr1 and right < lengthArr2:
        if arr1[left] == None:
            left += 1
        elif arr2[right] == None:
            right += 1
        elif arr1[left] < arr2[right]:
            left += 1
        elif arr2[right] < arr1[left]:
            right += 1
        else:
            temp.append(arr1[left])
            left += 1
            right += 1
    return temp


# testcase 1
a1 = [1, 6, 9, 10, 11, 21]
b1 = [2, 6, 9, 11, 17, 21]


# testcase 2
a2 = []
b2 = [1, 2, 3]

# testcase 3
a3 = [None, None, None, 4, 5]
b3 = [1, None, 3, 4, 5]

# testcase 4
a4 = [1]
b4 = [1]

# testcase 5
a5 = [3,5,6,8,10,23]
b5 = [3,5,5,7,9,33,59,99]

# testcase 6
a6 = []
b6 = []

print(find_duplicates3(a1,b1))
print(find_duplicates3(a3, b3))