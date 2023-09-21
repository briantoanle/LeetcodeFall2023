


def testCase1():
    s = 'leetcode'
    wordDict = ['leet','code']

    wordBreak(s,wordDict)
def testCase2():
    s = "catsandog "
    wordDict = ["cats","dog","sand","and","cat"]
    print(wordBreak(s,wordDict))

def testCase3():
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    wordBreak(s,wordDict)

def testCase4():
    s = "aaaaaaa"
    wordDict = ["aaaa", "aaa"]
    print(wordBreak(s,wordDict))

def testCase5():
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    print(wordBreak(s,wordDict))
def wordBreak2(s,wordDict):
    print(s,wordDict)
    temp = ''
    left,right = 0,1
    while right < len(s)+1:
        #print(s[left:right])
        if s[left:right] in wordDict:
            temp += s[left:right]
            left = right

        #print(s[left:right])
        right += 1
    print(temp)
    if len(temp) == len(s):
        print('hereeee')
        return True
    return False
    # leetcode


def wordBreak(s,wordDict,memo = {}):
    # print(s)
    if s in memo:
        return False
    if s == "":

        return True
    for word in wordDict:
        if s.startswith(word) is True:
            if wordBreak(s[len(word):], wordDict,memo) is True:
                return True

    memo[s] = False
    # print("string False:", s)
    return False

"""
                leetcode
                    |-leet
                   code
                    !-code
                    "" True 



                applepenapple
                    |-apple
                  penapple
                    |-pen
                   apple
                    |-apple
                    "" True


                aaaaaaa  ['aaaa','aaa']
            /-aaaa     \-aaa
          aaa          aaaa 
           |-aaa         |-aaaa
           "" True


                catsandog
            /-cats         \-cat
           andog            sandog
            |-and             |-sand  
            og False         og False



"""
testCase5()