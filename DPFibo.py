def fib(n):
    list=[0,1]
    for i in range(2,n+1):
        list.append(list[i-1]+list[i-2])
    return list[n]
def i(list):
    
    
    list.remove(2)
    print (list)

list=[2,3,4,3]
i(list)
#print (fib(50))