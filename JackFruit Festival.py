n,d=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse="True")
s=0
for i in range(d):
       s+=l[i]
print(s)
