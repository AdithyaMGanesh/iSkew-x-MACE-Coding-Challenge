n=int(input())
reg=0
lis=[]
val_list=[]
for j in range(n):
    lis.append(list(map(str,input().split())))
i=0
while i<n:
    if lis[i][0]=='PUSH':
        val_list.append(int(lis[i][1]))

    elif lis[i][0]=="STORE":
        if val_list:
            reg=val_list[-1]
            val_list.pop()
            
    elif lis[i][0]=="LOAD":
        val_list.append(reg)

    elif lis[i][0]=="PLUS":
        if len(val_list)>=2:
            sum_val=val_list[-1]+val_list[-2]
            val_list.pop()
            val_list.pop()
            val_list.append(sum_val)

    elif lis[i][0]=="IFZERO":
        if val_list:
            val=val_list.pop()
            if val==0:
                i=int(lis[i][1])
                continue

    elif lis[i][0]=="TIMES":
        if len(val_list)>=2:
            mul_val=val_list[-1]*val_list[-2]
            val_list.pop()
            val_list.pop()
            val_list.append(mul_val)

    elif lis[i][0]=="DONE":
        break
    i+=1
print(val_list[-1])
