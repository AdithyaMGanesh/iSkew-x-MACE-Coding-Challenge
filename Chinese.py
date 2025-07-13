n=int(input())
day=list(map(int,input().split()))
night=list(map(int,input().split()))
time=int(input())
day.sort()
night.sort(reverse="True")
count=0
for i in range(n):
    sumval=day[i]+night[i]
    if sumval>time:
        val=sumval-time
        count+=val
newval=count*100
print(newval)
