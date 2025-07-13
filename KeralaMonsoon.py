n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
s=[]
s.append(l[0])
for i in range(1,n):
    if abs(s[-1][0]-l[i][0]) <= s[-1][1]-l[i][1]:
        continue  
    elif abs(l[i][0]-s[-1][0])<= l[i][1]-s[-1][1]:
        s.pop()
        s.append(l[i])
    else:
        s.append(l[i])
print(len(s))
    


