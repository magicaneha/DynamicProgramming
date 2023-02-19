# Time complexity O(nc) where n is number of item and c is capacity
def knapsackProblem(item,capacity):
    #initalizing the 2d array
    knapsackValues= [[0 for x in range(0,capacity+1)]for y in range(0,len(item)+1)]

    for i in range(1, len(item)+1):
        currentWeight=item[i-1][1]
        currentValue= item[i-1][0]
        for c in range(0,capacity+1):
            if currentWeight>c:
                knapsackValues[i][c]=knapsackValues[i-1][c]
            else:
                knapsackValues[i][c]= max(knapsackValues[i-1][c],knapsackValues[i-1][c-currentWeight]+currentValue)
    return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues,item)]
def getKnapsackItems(knapsackValues,item):
    sequence=[]
    i = len(knapsackValues)-1
    c = len(knapsackValues[0])-1
    while i>0:
        if knapsackValues[i][c]== knapsackValues[i-1][c]:
            i-=1
        else:
            sequence.append(i-1)
            i-=1
            c-=item[i-1][1]
        if c==0:
            break
    return list(reversed(sequence))




    





item=[
  [1, 3],
  [4, 3],
  [5, 6],
  [6, 7]
]
capacity=10
print (knapsackProblem(item,capacity))