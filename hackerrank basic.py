usernames = ["bee","superhero","ace"]

#print( 'a' > 'b')
s = 'caberqiitefg'
k = 5

s1 = 'aeiouia'
k1 = 3

def findSubstring(string,length):
    print(len(string))
    finalStr = ''
    finale = 0

    for i in range(len(string)-length+1):
        total = 0
        dictionary = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        for j in string[i:i+length]:
            if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
                total+=1
            print(j,end=' ')
        print('total',total)

        print()
        if total > finale:
            finale = total
            finalStr = string[i:i+length]
        '''if len(finalStr) == length:
            return finalStr'''
    return finalStr

def findSubstring(s,k):

    first = s[0:k]
    print(first)
    


findSubstring(s,k)
#findSubstring(s1,k1)