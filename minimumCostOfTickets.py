'''
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive trave
'''''
def minCost(days,costs):
    dp ={}
    def dfs(i):
        if i == len(days):
            return 0
        if i in dp:
            return dp[i]
        dp[i]=float("inf")
        for d,c in zip([1,7,30],costs):
            j=i
            while j<len(days) and days[j]<days[i]+d:
                j+=1
            dp[i]= min (dp[i], c+dfs(j))
        return dp[i]
    return dfs(0)
days=[1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
print(minCost(days,costs))