#Given a string s, return the longest palindromic substring in s.


def longestPalindrome(s):
    
    resultString=''
    reslength=0
    for i in range(len(s)):
        #odd length
        leftPointer=i
        rightPointer=i
        while (leftPointer>=0 and rightPointer<len(s) and s[leftPointer]==s[rightPointer]):
            if rightPointer-leftPointer+1>reslength:
                resultString=s[leftPointer:rightPointer+1]
                reslength=rightPointer-leftPointer+1
            leftPointer-=1
            rightPointer+=1
        #even length string
        leftPointer=i
        rightPointer=i+1
        while (leftPointer>=0 and rightPointer<len(s) and s[leftPointer]==s[rightPointer]):
            if rightPointer-leftPointer+1>reslength:
                resultString=s[leftPointer:rightPointer+1]
                reslength=rightPointer-leftPointer+1
            leftPointer-=1
            rightPointer+=1       
    return resultString

print(longestPalindrome("adbdasbndsaddas"))