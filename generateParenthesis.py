'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

def generateParenthesis(n):
    #only add open parenthsis if open<n
    #only add a closing parenthesis if closed <open
    #valid if open==closed==n
    stack=[]
    result=[]
    def backTrack(openN,closeN):
        if openN==closeN==n:
           result.append( "".join(stack))
        if openN<n:
            stack.append("(")
            backTrack(openN+1,closeN)
            stack.pop()
        if closeN<openN:
            stack.append(")")
            backTrack(openN,closeN+1)
            stack.pop()
    backTrack(0,0)  
    return result      
print (generateParenthesis(4))


