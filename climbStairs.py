#climbing stair problem
#n is steps to reach to the tops
#how many different way you can reach to the top when you can clim either or two steps at a time
def climbingStair(n):
    one=1
    two=1
    for i in range(n-1):
        one,two=two,one+two
    return two
value=climbingStair(10)
print (value)