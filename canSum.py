def canSum(target,list):
    #recursive approach
    if target==0:
        return True
    if target<0:
        return False
    for i in list:
        rem=target-i
        
        if canSum(rem,list)==True:
            return True
    return False


list=[5,2,3]
print(canSum(4,list))