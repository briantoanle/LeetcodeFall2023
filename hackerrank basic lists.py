'''if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        a = input()
        temp = a.split()

        if temp[0] == 'insert':
            arr.insert(int(temp[1]), int(temp[2]))
        elif temp[0] == 'remove':
            arr.remove(temp[1])
        elif temp[0] == 'append':
            arr.append(temp[1])
        elif temp[0] == 'sort':
            arr.sort()
        elif temp[0] == 'print':
            print(arr)
        elif temp[0] == 'pop':
            arr.pop()
        elif temp[0] == 'reverse':
            arr.reverse()'''


def grades(grades):
    #if grades < 38:
        #return grades

    base = grades // 10
    rem = base * 10
    temp = (rem-base) //5
    print(base,rem,temp)
    #print(base,rem,grades)
    if rem == 3:
        return grades + grades % 5
    else:
        return grades


print(grades(73))
print(grades(67))
print(grades(38))
print(grades(33))
